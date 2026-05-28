# Guía de Autodefensa Dixital (Web & Ebook)

> **Por que facemos esta guía?** Vivimos nun mundo que, coa súa parte boa e a súa parte mala, vaise movendo cara o lado dixital a pasos axigantados, e en ocasións deixando a moita xente atrás. Este mundo dixital, ao igual ca o presencial, tamén ten unha serie de riscos dos que protexerse. Moitas de vós quizais tedes a esa persoa de confianza (filla, sobriña, amiga...) a quen consultarlle dúbidas ou pedir consello en cousas relacionadas coas tecnoloxías da información (TIC), pero non todo o mundo ten esa opción.
>
> É por iso que facemos esta guía, explicando de forma clara e detallada como podes mellorar a túa seguridade dixital, teñas ou non coñecementos previos de ciberseguridade. Antes de comezar, é importante ter claro que a seguridade absoluta non existe, e sempre hai risco. O que podemos facer como persoas usuarias é poñer barreiras que nos protexan.
>
> Esta é unha guía dinámica. É dicir, irémola actualizando a medida que nos vaian chegando suxestións. En [https://i.gal/autodefensadixital](https://i.gal/autodefensadixital) poderás consultar sempre a última versión da guía.
>
> Máis información en: [Blog de Enxeñería Sen Fronteiras Galicia](https://galicia.isf.es/blog/guia-de-autodefensa-dixital-recupera-a-tua-soberania-dixital/)

---

Este repositorio contén a versión en **Markdown** da Guía de Autodefensa Dixital, lista para ser publicada como sitio web e en formato libro electrónico (EPUB). O proxecto foi migrado dende o LaTeX orixinal empregando scripts automatizados.

## Estrutura do Proxecto

- **`docs/`**: Contén os ficheiros Markdown co contido da guía.
  - **`docs/gl/`**: Guía en Galego (versión principal). Inclúe os subdirectorios `imaxes/` e `logos/`.
  - **`docs/es/`**: Guía en Castellano. Inclúe os subdirectorios `imaxes/` e `logos/`.
  - **`docs/index.md`**: Páxina de inicio/portal cun selector de idioma visual e premium.
  - **`docs/stylesheets/extra.css`**: Ficheiro CSS coas cores corporativas e estilo personalizado.
- **`zensical.toml`**: Ficheiro de configuración do xerador de sitios estáticos Zensical.
- **`tools/`**: Pasta no directorio raíz coas ferramentas e scripts de automatización:
  - `convert.py`: Script para converter o LaTeX orixinal a Markdown GFM.
  - `export_epub.py`: Script para xerar os libros electrónicos (EPUB) en ambas linguas.

---

## Requisitos de Desenvolvemento

Este proxecto emprega **`uv`** para xestionar dependencias e a contorna virtual de Python.

1. Instalar `uv` (se non está dispoñible):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
2. Asegurar que `pandoc` está instalado no sistema.

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
3. Abre o teu navegador en `http://localhost:8000`.

---

## Como Construír o Sitio de Produción

```bash
.venv/bin/zensical build
```

---

## Como Exportar en Formato Libro Electrónico (EPUB)

```bash
python3 ../tools/export_epub.py
```
