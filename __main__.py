import bitdeli
from bitdeli.widgets import Group, Text, Bar, set_theme

import random
from zipfile import ZipFile

for profile in bitdeli.profiles():
    pass

random.seed(1)
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


# slide 7

Text(head='Bitdeli does NOT',
     size=(12, 2))
Text(head='Scale to the largest datasets',
     size=(12, 1),
     color=2)
Text(head='Provide the lowest latencies',
     size=(12, 1),
     color=2)
Text(head='Target any vertical in particular',
     size=(12, 1),
     color=2)
Text(head='Produce the prettiest visualizations',
     size=(12, 1),
     color=2)

# slide 8 

for i in range(10):
    Text(head='why?',
         size=(random.randint(1, 4), 2),
         color=random.randint(0, 3))
Text(head='',
     size=(12, 2))

# slide 9

Text(head='Infrastructure for ',
     size=(5, 2))
Text(head='Big Data',
     size=(4, 2),
     color=2)
Text(head='is becoming',
     size=(3, 2))
Text(head='a commodity',
     size=(12, 6),
     color=2)

# slide 10

Text(head='Integrating ',
     size=(8, 2))
Text(head='data',
     size=(4, 3),
     color=2)
Text(head='to business',
     size=(5, 5),
     color=2)
Text(head='is almost as hard as it has ever been',
     size=(7, 2))

# slide 11

Text(head='Who are in the best position',
     size=(12, 2))
Text(head='to solve this problem in the companies?',
     size=(12, 2))
Text(head='CEOs?',
     size=(3, 3),
     color=0)
Text(head='CIOs?',
     size=(3, 3),
     color=1)
Text(head='Business Analysts?',
     size=(6, 5),
     color=2)

# slide 12

Text(head='Hackers.',
     size=(12, 4))
Text(head='(given the right tools)',
     size=(12, 1),
     color=2)
Text(head='',
     size=(12, 3))

# slide 13
Text(head='why hackers?',
     size=(12, 3))
Text(head='',
     size=(5, 3))
Text(head='==',
     size=(7, 3),
     color=2)
Text(head='why Bitdeli?',
     size=(12, 3))