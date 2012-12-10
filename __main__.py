import bitdeli
from bitdeli.widgets import Group, Text, Bar, set_theme

from zipfile import ZipFile

for profile in bitdeli.profiles():
    pass

set_theme('playground')

# slide 1

Text(head='',
     size=(12, 1))
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

# slide 4

Text(head='why?',
     size=(12, 3))

g_trendy = Group(layout='horizontal')
Text(head='Bitdeli is the',
     size=(3, 3),
     group=g_trendy)
Text(head='531st',
     size=(3, 5),
     color=2,
     group=g_trendy)
Text(head='trendy analytics startup',
     size=(6, 3),
     group=g_trendy)

# slide 5

corpdataraw = ZipFile('/tmp/worker').read('data/companies-by-year.txt')
corpdata = [map(int, reversed(line.strip().split()))
            for line in corpdataraw.splitlines()]
total = sum(count for year, count in corpdata)
Bar(data=corpdata,
    size=(12, 3),
    color=1)
Text(head='Total 2007-2012:',
     size=(6, 1))
Text(head='%d new analytics startups' % total,
     size=(12, 4),
     color=2)

# slide 6

hadpdataraw = ZipFile('/tmp/worker').read('data/hadoop-by-year.txt')
hadpdata = [map(int, reversed(line.strip().split()))
            for line in hadpdataraw.splitlines()]
total = sum(count for year, count in hadpdata)
Bar(data=hadpdata,
    size=(12, 3),
    color=1)
Text(head='Total 2007-2012:',
     size=(6, 1))
Text(head='%d Hadoop startups' % total,
     size=(12, 4),
     color=2)