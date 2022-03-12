# orthodox-bible
### Scripts to compile an Orthodox Bible

Run `python txt2json.py` to generate a JSON file from the source text.

Run `python json2tex.py` to generate a LaTeX file from the output of `txt2json.py`.

Run `pdflatex bible.tex` to generated a PDF from the output of `json2tex.py`.

Run `python json2html.py` to generate a single-page HTML file from the output of `txt2json.py`.

Simple as.

If you want to use different source translations, you'll probably need to fix `book_order` in `txt2json.py`. I got my translations from [ebible.org](https://ebible.org/)
