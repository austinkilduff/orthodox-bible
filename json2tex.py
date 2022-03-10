import json
from collections import OrderedDict
from utils import clean_str

latex_contents = '''\\documentclass[twocolumn]{article}
\\usepackage{titlesec}
\\usepackage[T1]{fontenc}
\\usepackage[letterpaper, portrait, margin=0.5in]{geometry}

\\titleformat{\section}
{\\Huge\\bfseries\\filcenter}
{}
{0em}
{}
\\titleformat{\subsection}
{\\Large\\bfseries}
{}
{0em}
{}
\\titleformat{\subsubsection}[runin]
{\\bfseries}
{}
{0em}
{}

\\begin{document}
'''

with open('bible.json') as f:
    bible = json.loads(f.read(), object_pairs_hook=OrderedDict)
    for book_title in bible:
        latex_contents += '\n'
        latex_contents += '\\section{' + clean_str(book_title) + '}'
        for chapter_number in bible[book_title]:
            latex_contents += '\n'
            latex_contents += '\\subsection{Chapter ' + clean_str(chapter_number) + '}'
            for verse_number in bible[book_title][chapter_number]:
                latex_contents += '\n'
                latex_contents += '\\subsubsection{' + clean_str(verse_number) + '}'
                latex_contents += '\n'
                latex_contents += clean_str(bible[book_title][chapter_number][verse_number])
        latex_contents += '\n'
        latex_contents += '\\clearpage'

latex_contents += '\n'
latex_contents += '\\end{document}'

with open('bible.tex', 'w') as f:
    f.write(latex_contents)
