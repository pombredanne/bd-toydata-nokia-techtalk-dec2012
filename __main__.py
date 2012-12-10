import bitdeli
from bitdeli.widgets import Users, Map, Group, Text, Bar, set_theme

import random
from zipfile import ZipFile

HASHES = ['205e460b479e2e5b48aec07710c08d50',
          '25c7c18223fb42a4c6ae1c8db6f50f9b',
          'x',
          'f0a7bfdc9c509e8ea02b3ad25ba768b6',
          'b42c651650ec8d3d95829c75e318af2d',
          'd0ae789ef12347de8ec30b3765dd5d89',
          'x',
          '476d8afffbfa06fa852e677848c2388d']

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
     size=(5, 4),
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
Text(head='',
     size=(12, 2))

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
     size=(12, 2))
Text(head='',
     size=(3, 2))
Text(head='==',
     size=(9, 2),
     color=2)
Text(head='why Bitdeli?',
     size=(12, 2))
Text(head='',
     size=(12, 3))

# slide 14

Text(head='1) Customize',
     size=(12, 8),
     color=3)

# slide 15

Text(head='2) Experiment',
     size=(12, 8),
     color=3)

# slide 16

Text(head='3) Share',
     size=(12, 8),
     color=3)

# slide 17

Text(head='Why Bitdeli is the easiest way to',
     size=(12, 2))
Text(head='hack custom analytics?',
     size=(12, 7),
     color=2)

# slide 18

Text(head='1) Simple Python',
     size=(12, 8),
     color=1)

# slide 19

Text(head='2) User-Centric',
     size=(12, 8),
     color=1)

# slide 20

Text(head='3) Built-in Visualizations',
     size=(12, 2),
     color=1)

g_left = Group(layout='vertical')
g_right = Group(layout='vertical')

Map(size=(6, 5),
    data={'IN': 30},
    color=2,
    group=g_left)

def bar_data():
    for i, month in enumerate(['%.2d/11' % m for m in range(6, 13)] +
                              ['%.2d/12' % m for m in range(1, 3)]):
        yield month, 100 + abs(i - 6) * 25 + random.randint(1, 50)

Bar(size=(6, 3),
    color=1,
    data=list(bar_data()),
    group=g_right)

Users(size=(6, 2),
      large=True,
      data=[{'gravatar_hash': h} for h in HASHES],
      group=g_right)

Text(head='',
     size=(12, 3))

# slide 21

Text(head='4) Real-Time',
     size=(12, 8),
     color=1)

# slide 22

Text(head='5) Solid Platform',
     size=(12, 8),
     color=1)

# slide 23

Text(head='Thank You!',
     size=(12, 2),
     color=1)
Text(head='Sign Up for FREE at',
     size=(12, 2),
     color=2)
Text(head='bitdeli.com',
     size=(12, 2),
     color=1)
Text(head='',
     size=(12, 5))