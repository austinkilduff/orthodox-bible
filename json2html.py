import json
from collections import OrderedDict
from utils import clean_str, html_str

html_contents = '<html><body><h1>The Holy Bible</h1><ul>'

with open('bible.json') as f:
    bible = json.loads(f.read(), object_pairs_hook=OrderedDict)

    for book_title in bible:
        html_contents += '<li><a href="#' + html_str(book_title) + '">' + book_title + '</a></li>'
    html_contents += '</ul>'

    for book_title in bible:
        html_contents += '<h2 id="' + html_str(book_title) + '">' + clean_str(book_title) + '</h2>'

        for chapter_number in bible[book_title]:
            html_contents += '<a href="#' + html_str(book_title + str(chapter_number)) + '">' + str(chapter_number) + '</a> '

        for chapter_number in bible[book_title]:
            html_contents += '<h3 id="' + html_str(book_title + str(chapter_number)) + '">Chapter ' + clean_str(chapter_number) + '</h3>'
            for verse_number in bible[book_title][chapter_number]:
                html_contents += '<b>' + clean_str(verse_number) + ' </b>'
                html_contents += clean_str(bible[book_title][chapter_number][verse_number]) + '</br>'

html_contents += '</body></html>'

with open('bible.html', 'w') as f:
    f.write(html_contents)
