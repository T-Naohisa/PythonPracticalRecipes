import re

print(re.search('a.c', 'abcdef'))
print(re.match('a.c', 'abcdef'))

# complieのほうが処理が早い
pattern = re.compile('a.c')
print(pattern.search('abcdef'))

regex2 = re.compile('[-+()]')
print(regex2.split('080-1234-5678'))
