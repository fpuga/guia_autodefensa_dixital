#!/usr/bin/env python3
import os
import re
import subprocess

# Paths
BASE_DIR = "/home/fpuga/development/try/guia"
DOCS_DIR = os.path.join(BASE_DIR, "miguia", "docs")

def run_command(cmd, cwd=None):
    result = subprocess.run(cmd, shell=True, text=True, capture_output=True, cwd=cwd)
    if result.returncode != 0:
        print(f"Command failed: {cmd}")
        print(f"Error: {result.stderr}")
    return result.returncode == 0

def preprocess_for_pdf(content):
    # Remove HTML anchors/spans
    content = re.sub(r'<span id="[^"]+"></span>', '', content)
    
    # Convert HTML links inside figures or text back to markdown links
    content = re.sub(r'<a href="([^"]+)"[^>]*>(.*?)</a>', r'[\2](\1)', content)

    # Convert figures to standard Markdown images
    content = re.sub(
        r'<figure>\s*<img src="([^"]+)"[^>]*/>\s*<figcaption>(.*?)</figcaption>\s*</figure>',
        r'![\2](\1)',
        content,
        flags=re.DOTALL
    )

    # Convert normal <img> tags to markdown images
    content = re.sub(r'<img src="([^"]+)"[^>]*alt="([^"]+)"[^>]*>', r'![\2](\1)', content)
    content = re.sub(r'<img src="([^"]+)"[^>]*>', r'![](\1)', content)

    # Strip logos from headers (e.g. lines starting with ### or ## containing ![]...)
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if line.strip().startswith('#'):
            lines[i] = re.sub(r'!\[.*?\]\(.*?\)', '', line).strip()
            lines[i] = re.sub(r'\s+', ' ', lines[i])
    content = '\n'.join(lines)

    return content

def export_book(lang, title, author, base_filename):
    lang_dir = os.path.join(DOCS_DIR, lang)
    if not os.path.exists(lang_dir):
        print(f"Language directory {lang_dir} does not exist.")
        return

    chapters = [
        "introducion.md",
        "servizos_libres.md",
        "fediverso.md",
        "rss_feed.md",
        "nube.md",
        "contrasinais.md",
        "vpn_proxy_tor.md",
        "dns.md",
        "navegador.md",
        "wifi.md",
        "phishing.md",
        "sistemas_operativos.md",
        "smartphones.md",
        "compras.md",
        "uso_en_organizacions.md",
        "mobiles_adolescentes.md",
        "outra_material_de_interese.md"
    ]

    # --- 1. Export EPUB ---
    input_files_epub = []
    for ch in chapters:
        path = os.path.join(lang_dir, ch)
        if os.path.exists(path):
            input_files_epub.append(f'"{path}"')

    if input_files_epub:
        input_files_str = " ".join(input_files_epub)
        epub_output_path = os.path.join(BASE_DIR, "miguia", f"{base_filename}.epub")
        epub_cmd = f'pandoc {input_files_str} -o "{epub_output_path}" --toc --metadata title="{title}" --metadata author="{author}" --metadata language="{lang}"'
        print(f"Compiling EPUB for {lang}...")
        if run_command(epub_cmd, cwd=lang_dir):
            print(f"Successfully generated EPUB: {epub_output_path}")
        else:
            print(f"Failed to generate EPUB for {lang}.")
    else:
        print(f"No chapters found for EPUB export in {lang}.")

    # --- 2. Export PDF ---
    concatenated_content = f"""---
title: "{title}"
author: "{author}"
lang: {lang}
toc: true
geometry: margin=2.5cm
---

"""

    for ch in chapters:
        path = os.path.join(lang_dir, ch)
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                ch_content = f.read()
            processed = preprocess_for_pdf(ch_content)
            concatenated_content += processed + "\n\n"

    temp_md_path = os.path.join(lang_dir, "temp_pdf_book.md")
    with open(temp_md_path, "w", encoding="utf-8") as f:
        f.write(concatenated_content)

    pdf_output_path = os.path.join(BASE_DIR, "miguia", f"{base_filename}.pdf")
    pdf_cmd = f'pandoc "temp_pdf_book.md" -o "{pdf_output_path}" --pdf-engine=pdflatex'
    print(f"Compiling PDF for {lang}...")
    
    pdf_success = False
    try:
        pdf_success = run_command(pdf_cmd, cwd=lang_dir)
    finally:
        if os.path.exists(temp_md_path):
            os.remove(temp_md_path)

    if pdf_success:
        print(f"Successfully generated PDF: {pdf_output_path}")
    else:
        print(f"Failed to generate PDF for {lang}.")

def main():
    # Galician Version
    export_book(
        lang="gl",
        title="Guía de Autodefensa Dixital",
        author="Enxeñería Sen Fronteiras Galicia",
        base_filename="guia_autodefensa_dixital"
    )

    # Spanish Version
    export_book(
        lang="es",
        title="Guía de Autodefensa Digital",
        author="Enxeñería Sen Fronteiras Galicia",
        base_filename="guia_autodefensa_digital"
    )

if __name__ == "__main__":
    main()
