# Directorio de Ferramentas (Tools)

Este directorio contén scripts e ferramentas automatizadas para converter e exportar a Guía de Autodefensa Dixital.

## Ficheiros

- **`convert.py`**:
  Este script realiza a conversión automatizada de LaTeX (`.tex`) a Markdown GFM (`.md`) para as dúas versións (Galego e Castellano):
  1. Escanea todos os ficheiros LaTeX en busca de referencias cruzadas (`\label{...}`) e xera un mapeo dinámico ao seu correspondente ficheiro Markdown e título do encabezado.
  2. Preprocesa os ficheiros `.tex` para aliñar os logos integrados dentro dos títulos e listas en formato compatible con Markdown.
  3. Invoca a `pandoc` para a conversión a Markdown GFM.
  4. Postprocesa os ficheiros Markdown resultantes, transformando os enlaces HTML en enlaces Markdown funcionais empregando o mapeo dinámico e as áncoras correspondentes, eliminando lixo xerado e axustando rutas de imaxes relativas.
  5. Constrúe a páxina de inicio e indexación de ambos idiomas, e a páxina raíz con selector visual de idioma.
  - **Uso**:
    ```bash
    python3 tools/convert.py
    ```

- **`export_book.py`**:
  Este script compila os ficheiros Markdown xerados e ordenados na estrutura de `miguia/docs` en libros electrónicos (EPUB) e libros en formato PDF independentes para Galego e Castellano:
  - Establece a orde secuencial correcta dos capítulos definida nos ficheiros LaTeX principais.
  - Concatena e executa a compilación a EPUB e a PDF mediante `pandoc` (empregando o motor `pdflatex` instalado).
  - Preprocesa os contidos das páxinas para o formato PDF (eliminando lixo HTML, simplificando figuras a formato nativo markdown e eliminando as iconas dos títulos para un deseño de impresión de alta calidade).
  - **Uso**:
    ```bash
    python3 tools/export_book.py
    ```
