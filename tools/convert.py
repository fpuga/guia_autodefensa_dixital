#!/usr/bin/env python3
import os
import re
import shutil
import subprocess

# Paths
BASE_DIR = "/home/fpuga/development/try/guia"
TEX_DIR = os.path.join(BASE_DIR, "guia_autodefensa_dixital")
MIGUIA_DIR = os.path.join(BASE_DIR, "miguia")
DOCS_DIR = os.path.join(MIGUIA_DIR, "docs")

heading_label_pat = re.compile(r'\\(chapter|section|subsection|subsubsection|paragraph|textbf)\{(.+?)\s*\\label\{([^}]+)\}\}')
alone_label_pat = re.compile(r'\\label\{([^}]+)\}')
link_pat = re.compile(r'<a href="#(?P<label>[^"]+)"[^>]*>(?P<text>.*?)</a>')

def run_command(cmd, cwd=None):
    result = subprocess.run(cmd, shell=True, text=True, capture_output=True, cwd=cwd)
    if result.returncode != 0:
        print(f"Command failed: {cmd}")
        print(f"Error: {result.stderr}")
    return result.stdout

def scan_labels(dir_path):
    label_map = {}
    for root, dirs, files in os.walk(dir_path):
        for f in files:
            if f.endswith(".tex") and not f.endswith(".temp"):
                path = os.path.join(root, f)
                with open(path, "r", encoding="utf-8") as file:
                    content = file.read()
                
                # Find headings with labels
                for match in heading_label_pat.finditer(content):
                    level, title, label = match.groups()
                    # Clean title: strip LaTeX commands and spaces
                    clean_title = re.sub(r'\\[a-zA-Z]+(\[[^\]]*\])?({[^}]*})?', '', title)
                    clean_title = clean_title.replace("{", "").replace("}", "").strip()
                    label_map[label] = (f.lower().replace(".tex", ".md"), clean_title)
                
                # Find any other labels
                for match in alone_label_pat.finditer(content):
                    label = match.group(1)
                    if label not in label_map:
                        label_map[label] = (f.lower().replace(".tex", ".md"), "enlace")
    return label_map

def preprocess_latex(content):
    # Match: \href{URL}{\raisebox{SHIFT}{\includegraphics[ARGS]{LOGO}}TEXT}
    # Substitute with: \includegraphics[height=0.5cm]{LOGO} \href{URL}{TEXT}
    pattern_href_logo = r'\\href\{([^{}]+)\}\{\\raisebox\{[^{}]+\}\{\\includegraphics\[[^\]]*\]\{([^{}]+)\}\}([^}]+)\}'
    content = re.sub(pattern_href_logo, r'\\includegraphics[height=0.5cm]{\2} \\href{\1}{\3}', content)
    
    # General logo replacement for raisebox without href
    pattern_raisebox_logo = r'\\raisebox\{[^{}]+\}\{\\includegraphics\[[^\]]*\]\{([^{}]+)\}\}([^}]+)'
    content = re.sub(pattern_raisebox_logo, r'\\includegraphics[height=0.5cm]{\1} \2', content)

    return content

def postprocess_markdown(content, label_map, current_file):
    # Remove empty label tags like []{#cap:dns label="cap:dns"}
    content = re.sub(r'\[\]\{#cap:[^}]+}', '', content)
    content = re.sub(r'\[\]\{#[^}]+}', '', content)

    # Simplify span elements to standard HTML anchors
    content = re.sub(r'<span id="([^"]+)" label="[^"]+"></span>', r'<span id="\1"></span>', content)

    # Fix relative image paths starting with ./logos or ./imaxes
    content = re.sub(r'src="\./logos/', 'src="logos/', content)
    content = re.sub(r'src="\./imaxes/', 'src="imaxes/', content)
    content = re.sub(r'\(./logos/', '(logos/', content)
    content = re.sub(r'\(./imaxes/', '(imaxes/', content)

    # Replace HTML cross-reference links with clean Markdown links using mapped titles
    def repl(match):
        label = match.group("label")
        original_text = match.group("text").strip()
        if label in label_map:
            dest_file, title = label_map[label]
            # If title is generic "enlace", use original text
            link_text = original_text if title == "enlace" else title
            # Clean brackets from original_text if any (e.g. [cap:dns] -> cap:dns)
            link_text = link_text.strip("[]")
            if dest_file == current_file:
                return f"[{link_text}](#{label})"
            else:
                return f"[{link_text}]({dest_file}#{label})"
        else:
            return match.group(0)

    content = link_pat.sub(repl, content)

    # Convert .pdf image links to .svg in output markdown images
    content = re.sub(r'\.pdf\b', '.svg', content)
    return content

def convert_file(src_path, dest_path, label_map):
    print(f"Converting {src_path} -> {dest_path}")
    with open(src_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Pre-process LaTeX
    preprocessed = preprocess_latex(content)

    # Write to a temp file
    temp_tex = src_path + ".temp"
    with open(temp_tex, "w", encoding="utf-8") as f:
        f.write(preprocessed)

    try:
        # Run pandoc GFM
        run_command(f'pandoc -f latex -t gfm "{temp_tex}" -o "{dest_path}" --wrap=none')
    finally:
        if os.path.exists(temp_tex):
            os.remove(temp_tex)

    # Post-process Markdown
    if os.path.exists(dest_path):
        with open(dest_path, "r", encoding="utf-8") as f:
            md_content = f.read()
        
        current_file = os.path.basename(dest_path)
        postprocessed = postprocess_markdown(md_content, label_map, current_file)
        
        with open(dest_path, "w", encoding="utf-8") as f:
            f.write(postprocessed)

def build_index_page(lang, gl_docs_dir, es_docs_dir):
    if lang == "gl":
        title = "Guía de Autodefensa Dixital"
        intro_file = os.path.join(gl_docs_dir, "introducion.md")
        index_file = os.path.join(gl_docs_dir, "index.md")
        license_html = """---

<div align="center" style="margin-top: 50px; opacity: 0.85;">
  <img src="imaxes/esf_transparente_negro.png" alt="ESF" width="200" /><br>
  <p style="font-size: 0.9em; margin-top: 15px;">
    <a href="https://i.gal/autodefensadixital">Guía de autodefensa dixital</a> © 2025 por <a href="https://galicia.isf.es">Enxeñería Sen Fronteiras Galicia</a> está baixo a licenza <a href="https://creativecommons.org/licenses/by/4.0/deed.gl">CC BY 4.0</a>.
  </p>
</div>
"""
    else:
        title = "Guía de Autodefensa Digital"
        intro_file = os.path.join(es_docs_dir, "introducion.md")
        index_file = os.path.join(es_docs_dir, "index.md")
        license_html = """---

<div align="center" style="margin-top: 50px; opacity: 0.85;">
  <img src="imaxes/esf_transparente_negro.png" alt="ESF" width="200" /><br>
  <p style="font-size: 0.9em; margin-top: 15px;">
    <a href="https://i.gal/autodefensadigital">Guía de autodefensa digital</a> © 2025 por <a href="https://galicia.isf.es">Enxeñería Sen Fronteiras Galicia</a> está bajo la licencia <a href="https://creativecommons.org/licenses/by/4.0/deed.es">CC BY 4.0</a>.<br>
    Traducida al castellano por la Oficina de Software Libre de la Universidad de Zaragoza <a href="https://osluz.unizar.es">OSLUZ</a>.
  </p>
</div>
"""

    with open(intro_file, "r", encoding="utf-8") as f:
        intro_content = f.read()

    # Strip the leading title from the introduction markdown if it exists
    intro_content = re.sub(r'^#\s+.*', '', intro_content).strip()

    header_html = f"""# {title}

<div align="center" style="margin-bottom: 30px;">
  <img src="imaxes/soberania_dixital.svg" alt="Soberanía Dixital" width="100%" style="max-width: 600px; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);" />
</div>

"""

    final_content = header_html + intro_content + "\n\n" + license_html
    with open(index_file, "w", encoding="utf-8") as f:
        f.write(final_content)

def build_root_selector_page():
    root_index = os.path.join(DOCS_DIR, "index.md")
    content = """# Guía de Autodefensa Dixital

<div style="text-align: center; margin-top: 30px; margin-bottom: 20px;">
  <h2 style="font-weight: 500; font-size: 1.5em; opacity: 0.9;">Benvida/o á Guía de Autodefensa Dixital<br><span style="font-size: 0.85em; font-weight: 300;">Bienvenido/a a la Guía de Autodefensa Digital</span></h2>
  <p style="margin-bottom: 40px; opacity: 0.7;">Selecciona o idioma para ler a guía / Selecciona el idioma para leer la guía:</p>
</div>

<div style="display: flex; gap: 30px; justify-content: center; margin-top: 20px; flex-wrap: wrap; margin-bottom: 50px;">
  <a href="gl/" style="text-decoration: none; color: inherit; width: 280px;">
    <div style="border: 1px solid #ff8700; border-radius: 12px; padding: 30px 24px; text-align: center; background: rgba(255,135,0,0.03); transition: transform 0.2s, box-shadow 0.2s; box-shadow: 0 2px 8px rgba(255,135,0,0.05);" onmouseover="this.style.transform='translateY(-6px)'; this.style.boxShadow='0 12px 24px rgba(255,135,0,0.15)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 2px 8px rgba(255,135,0,0.05)'">
      <h2 style="color: #ff8700; margin-top: 0; font-size: 1.6em; margin-bottom: 12px;">Galego</h2>
      <p style="font-size: 0.95em; opacity: 0.8; margin-bottom: 20px; min-height: 40px;">Accede á versión orixinal en lingua galega</p>
      <div style="background: #ff8700; color: white; padding: 10px 24px; border-radius: 6px; display: inline-block; font-weight: 600; font-size: 0.95em; transition: background 0.2s;">Ler Guía</div>
    </div>
  </a>
  <a href="es/" style="text-decoration: none; color: inherit; width: 280px;">
    <div style="border: 1px solid #ff8700; border-radius: 12px; padding: 30px 24px; text-align: center; background: rgba(255,135,0,0.03); transition: transform 0.2s, box-shadow 0.2s; box-shadow: 0 2px 8px rgba(255,135,0,0.05);" onmouseover="this.style.transform='translateY(-6px)'; this.style.boxShadow='0 12px 24px rgba(255,135,0,0.15)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 2px 8px rgba(255,135,0,0.05)'">
      <h2 style="color: #ff8700; margin-top: 0; font-size: 1.6em; margin-bottom: 12px;">Castellano</h2>
      <p style="font-size: 0.95em; opacity: 0.8; margin-bottom: 20px; min-height: 40px;">Accede a la versión traducida en lengua castellana</p>
      <div style="background: #ff8700; color: white; padding: 10px 24px; border-radius: 6px; display: inline-block; font-weight: 600; font-size: 0.95em; transition: background 0.2s;">Leer Guía</div>
    </div>
  </a>
</div>
"""
    with open(root_index, "w", encoding="utf-8") as f:
        f.write(content)
    print("Root language selector page created.")

def main():
    # Dynamic Scanning of labels for context-aware cross-referencing links
    print("Scanning LaTeX labels for both languages...")
    gl_label_map = scan_labels(os.path.join(TEX_DIR, "capitulos"))
    es_label_map = scan_labels(os.path.join(TEX_DIR, "Outras_Linguas", "ES", "capitulos"))

    # Clean and create directories
    gl_docs_dir = os.path.join(DOCS_DIR, "gl")
    es_docs_dir = os.path.join(DOCS_DIR, "es")

    for d in [gl_docs_dir, es_docs_dir]:
        if os.path.exists(d):
            shutil.rmtree(d)
        os.makedirs(d, exist_ok=True)

    # Copy images and logos
    print("Copying assets...")
    shutil.copytree(os.path.join(TEX_DIR, "imaxes"), os.path.join(gl_docs_dir, "imaxes"), dirs_exist_ok=True)
    shutil.copytree(os.path.join(TEX_DIR, "logos"), os.path.join(gl_docs_dir, "logos"), dirs_exist_ok=True)
    
    shutil.copytree(os.path.join(TEX_DIR, "Outras_Linguas", "ES", "imaxes"), os.path.join(es_docs_dir, "imaxes"), dirs_exist_ok=True)
    shutil.copytree(os.path.join(TEX_DIR, "Outras_Linguas", "ES", "logos"), os.path.join(es_docs_dir, "logos"), dirs_exist_ok=True)

    # Ordered chapter lists
    chapters_gl = [
        "introducion", "servizos_libres", "fediverso", "rss_feed", "nube", 
        "contrasinais", "VPN_proxy_tor", "DNS", "navegador", "wifi", 
        "phishing", "sistemas_operativos", "smartphones", "compras", 
        "uso_en_organizacions", "mobiles_adolescentes", "outra_material_de_interese"
    ]

    chapters_es = [
        "introducion", "servizos_libres", "fediverso", "RSS_feed", "nube", 
        "contrasinais", "VPN_proxy_tor", "DNS", "navegador", "wifi", 
        "phishing", "sistemas_operativos", "smartphones", "compras", 
        "uso_en_organizacions", "mobiles_adolescentes", "outra_material_de_interese"
    ]

    # Convert Galician chapters
    for ch in chapters_gl:
        src = os.path.join(TEX_DIR, "capitulos", f"{ch}.tex")
        dest = os.path.join(gl_docs_dir, f"{ch.lower()}.md")
        convert_file(src, dest, gl_label_map)

    # Convert Spanish chapters
    for ch in chapters_es:
        src = os.path.join(TEX_DIR, "Outras_Linguas", "ES", "capitulos", f"{ch}.tex")
        dest = os.path.join(es_docs_dir, f"{ch.lower()}.md")
        convert_file(src, dest, es_label_map)

    # Construct the beautiful index.md homepages for gl and es
    build_index_page("gl", gl_docs_dir, es_docs_dir)
    build_index_page("es", gl_docs_dir, es_docs_dir)

    # Construct root portal selection page
    build_root_selector_page()

    print("All conversions and post-processing completed!")

if __name__ == "__main__":
    main()
