import re

title = 'meaning of life'
Title = list(title)
print(Title)
Title[0] = 'g'
print(Title)
print(''.join(Title))

line = 'aaa,bbb,ccc,dd,\n'
print line
print(line.split(','))
print(line.rstrip().split(','))
#print(line.split(',').rstrip()) changed object into list, rstrip not a list operation

print('%s, eggs, and %s' %('spam', 'SPAM!'))
print('{1}, eggs, and {0}'.format('spam', 'SPAM!'))
print('{}, eggs, and {}'.format('spam', 'SPAM!'))
print(dir(title))

print(re.split('[/:]', '/usr/home/nico'))
