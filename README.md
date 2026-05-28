# Guía de Autodefensa Dixital (Web & Ebook)

Este repositorio contén a versión en **Markdown** da Guía de Autodefensa Dixital, lista para ser publicada como sitio web e en formato libro electrónico (EPUB). O proxecto foi migrado dende o LaTeX orixinal empregando scripts automatizados.

## Estrutura do Proxecto

- **`docs/`**: Contén os ficheiros Markdown co contido da guía.
  - **`docs/gl/`**: Guía en Galego (versión principal). Inclúe os subdirectorios `imaxes/` e `logos/`.
  - **`docs/es/`**: Guía en Castellano. Inclúe os subdirectorios `imaxes/` e `logos/`.
  - **`docs/index.md`**: Páxina de inicio/portal cun selector de idioma visual e premium.
  - **`docs/stylesheets/extra.css`**: Ficheiro CSS coas cores corporativas e estilo personalizado.
- **`zensical.toml`**: Ficheiro de configuración do xerador de sitios estáticos Zensical (un sucesor moderno de Material para MkDocs baseado en Rust e Python).
- **`tools/`**: Pasta no directorio raíz coas ferramentas e scripts de automatización:
  - `convert.py`: Script para converter o LaTeX orixinal a Markdown GFM, corrixindo as referencias cruzadas e aliñando os logos nos títulos.
  - `export_epub.py`: Script para xerar os libros electrónicos (EPUB) en ambas linguas.

---

## Requisitos de Desenvolvemento

Este proxecto emprega **`uv`** para xestionar dependencias e a contorna virtual de Python.

1. Instalar `uv` (se non está dispoñible):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
2. Asegurar que `pandoc` está instalado no sistema (necesario para as conversións de LaTeX a Markdown e para exportar EPUB).

---

## Como Comezar e Servir Localmente

Para iniciar o servidor de desenvolvemento e ver a web interactiva en tempo real:

1. Crea e activa a contorna virtual e instala as dependencias:
   ```bash
   uv venv
   source .venv/bin/activate
   uv pip install zensical
   ```
2. Inicia o servidor local de Zensical:
   ```bash
   .venv/bin/zensical serve
   ```
3. Abre o teu navegador en `http://localhost:8000`. O servidor actualizará automaticamente calquera cambio que fagas nos ficheiros Markdown (Live Reload).

---

## Como Construír o Sitio de Produción

Para xerar o sitio web estático optimizado para produción (os ficheiros xerados gardaranse no directorio `site/`):

```bash
.venv/bin/zensical build
```

---

## Como Exportar en Formato Libro Electrónico (EPUB)

Para xerar os ficheiros EPUB das dúas versións da guía, executa o script da carpeta `tools`:

```bash
python3 ../tools/export_epub.py
```

Os ficheiros xerados gardaranse na raíz de `miguia/`:
- `guia_autodefensa_dixital.epub` (Galego)
- `guia_autodefensa_digital.epub` (Castellano)
