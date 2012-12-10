import bitdeli
from bitdeli.widgets import Group, Text, Bar, set_theme

from zipfile import ZipFile

for profile in bitdeli.profiles():
    pass

set_theme('playground')

# slide 1

Text(head='Bitdeli',
     size=(12, 3))
Text(head='Ville Tuulos | Co-Founder | CEO',
     size=(12, 4),
     color=2)

# slide 2

Text(head='',
     size=(12, 1))
Text(head='Easiest way to create',
     size=(12, 2))
Text(head='Custom Analytics',
     size=(12, 5),
     color=2)

# slide 3

g_ville = Group(layout='vertical')
g_pad = Group(layout='vertical')
g_jyri = Group(layout='vertical')

Text(head='',
     size=(2, 2),
     group=g_pad)

Text(head='Ville Tuulos',
     size=(5, 2),
     group=g_ville)
Text(head='Backend, CEO',
     size=(5, 1),
     group=g_ville)
Text(head='@NRC 2007-2011',
     size=(5, 1),
     group=g_ville,
     color=2)
Text(head='Team Lead, Data Insight',
     size=(5, 1),
     color=2,
     group=g_ville)
Text(head='Founder, Disco MapReduce',
     size=(5, 1),
     color=2,
     group=g_ville)

Text(head='Jyri Tuulos',
     size=(5, 2),
     group=g_jyri)
Text(head='Frontend',
     size=(5, 1),
     group=g_jyri)
Text(head='Tinkercad, Flowdock etc.',
     size=(5, 1),
     group=g_jyri,
     color=2)
Text(head='JS, Visualization hacker',
     size=(5, 3),
     group=g_jyri,
     color=2)

#Text(head='Why?',
#     size=(12, 12))
#
#Text(head='Bitdeli is the 531th 

print ZipFile('/tmp/worker').read('data/companies-by-year.txt')