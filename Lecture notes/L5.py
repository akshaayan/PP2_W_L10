import re

# hand = open('Lecture notes\mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     if re.search('From: ', line) :
#         x= re.search('From: .+\S', line)
#         print(x)

hand = open('Lecture notes\mbox-short2.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^X-.+:', line) :
        x= re.search('^X-.+:', line)
        print(x)

x = 'My 2 favorite \ numbers \ are 19 + 42 ooooo'
y = re.findall('[0-9]+',x)
print(y)
y = re.findall('[\\\]',x)
print(y)

st = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pattern = re.compile('[A-Z]..  [0-9].+')
print(pattern.findall(st))

