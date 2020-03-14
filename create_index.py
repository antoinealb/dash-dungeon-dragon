#!/usr/bin/env python3

import os, sqlite3, glob
from bs4 import BeautifulSoup

conn = sqlite3.connect('dnd.docset/Contents/Resources/docSet.dsidx')
cur = conn.cursor()

try:
    cur.execute('DROP TABLE searchIndex;')
except:
    pass

cur.execute('CREATE TABLE searchIndex(id INTEGER PRIMARY KEY, name TEXT, type TEXT, path TEXT);')
cur.execute('CREATE UNIQUE INDEX anchor ON searchIndex (name, type, path);')

for page in glob.glob('dnd.docset/Contents/Resources/Documents/*.html'):
    soup = BeautifulSoup(open(page).read(), features="html.parser")
    name = soup.find(class_="topicLineFirst").text
    path = os.path.basename(page)
    print("name: {} path: {}".format(name, path))
    cur.execute('INSERT OR IGNORE INTO searchIndex(name, type, path) VALUES (?,?,?)', (name, 'func', path))

conn.commit()
conn.close()
