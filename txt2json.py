import os
import json
from collections import OrderedDict

def clean_str(s):
    if s[0] not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789':
        s = s[1:]
    return s.strip()

ot_dir = 'Brenton_OldTestament'
nt_dir = 'DRA_NewTestament'
testament_dirs = [ot_dir, nt_dir]
bible = {}
book_titles = {}
for testament_dir in testament_dirs:
    testament_path = [txt_file for txt_file in os.listdir(testament_dir) if txt_file.endswith('.txt')]
    for chapter_file in testament_path:
        with open(os.path.join(testament_dir, chapter_file)) as f:
            chapter_contents = f.readlines()

            book_number = clean_str(chapter_file.split('_')[1])
            book_title = clean_str(chapter_contents[0].split('.')[0])
            if book_number not in book_titles:
                book_titles[book_number] = book_title
            elif len(book_title) > len(book_titles[book_number]):
                bible[book_title] = bible.pop(book_titles[book_number])
                book_titles[book_number] = book_title
            book_title = book_titles[book_number]

            chapter_number = int(clean_str(chapter_contents[1].split(' ')[1].split('.')[0]))

            if book_title not in bible:
                bible[book_title] = {}
            bible[book_title][chapter_number] = {}
            verse_number = 1
            for verse_line in chapter_contents[2:]:
                verse = clean_str(verse_line)
                if len(verse) > 0:
                    bible[book_title][chapter_number][verse_number] = verse
                    verse_number += 1

book_order = ['Genesis', 'Exodus', 'Leviticus', 'Numbers', 'Deuteronomy', 'Joshua', 'Judges', 'Ruth', 'Kings I', 'Kings II', 'Kings III', 'Kings IV', 'Chronicles I', 'Chronicles II', 'Ezra and Nehemiah', 'Esdras I', 'Nehemiah', 'Tobit', 'Judith', 'Esther (Greek)', 'Maccabees I', 'Maccabees II', 'Maccabees III', 'Maccabees IV', 'Psalms', 'The Prayer of Manasses', 'Job', 'Proverbs', 'Ecclesiastes', 'Song of Solomon', 'Wisdom of Solomon', 'Wisdom Of Jesus The Son Of Sirach (Ecclesiasticus)', 'Osee', 'Amos', 'Michæas', 'Joel', 'Obdias', 'Jonas', 'Naum', 'Ambacum', 'Sophonias', 'Aggæus', 'Zacharias', 'Malachias', 'Esaias', 'Jeremias', 'Baruch', 'Lamentations', 'Epistle of Jeremy', 'Jezekiel', 'Susanna', 'Daniel (Greek)', 'Bel and the Dragon', 'The Good News According to Matthew', 'The Good News According to Mark', 'The Good News According to Luke', 'The Good News According to John', 'The Acts of the Apostles', 'Paul’s Letter to the Romans', 'Paul’s First Letter to the Corinthians', 'Paul’s Second Letter to the Corinthians', 'Paul’s Letter to the Galatians', 'Paul’s Letter to the Ephesians', 'Paul’s Letter to the Philippians', 'Paul’s Letter to the Colossians', 'Paul’s First Letter to the Thessalonians', 'Paul’s Second Letter to the Thessalonians', 'Paul’s First Letter to Timothy', 'Paul’s Second Letter to Timothy', 'Paul’s Letter to Titus', 'Paul’s Letter to Philemon', 'The Letter to the Hebrews', 'The Letter from James', 'Peter’s First Letter', 'Peter’s Second Letter', 'John’s First Letter', 'John’s Second Letter', 'John’s Third Letter', 'The Letter from Jude', 'The Revelation to John']

sorted_bible = OrderedDict()
for book_title in book_order:
    sorted_bible[book_title] = bible.pop(book_title)

    chapter_numbers = sorted(list(sorted_bible[book_title].keys()))
    for chapter_number in chapter_numbers:
        sorted_bible[book_title][chapter_number] = sorted_bible[book_title].pop(chapter_number)

        verse_numbers = sorted(list(sorted_bible[book_title][chapter_number].keys()))
        for verse_number in verse_numbers:
            sorted_bible[book_title][chapter_number][verse_number] = sorted_bible[book_title][chapter_number].pop(verse_number)

json_file = 'bible.json'
with open(json_file, 'w') as f:
    f.write(json.dumps(sorted_bible))
