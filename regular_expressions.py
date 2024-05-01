import re

# str = 'cowwai bawwai hodama yaluwo denna!'
# y = re.findall('\d',str)
# print('d:',y)
# print('---------------------')
# y = re.findall('\w',str)
# print('w:',y)
# print('---------------------')
# y = re.findall('\W',str)
# print('W:',y)
# print('---------------------')
# y = re.findall('\s',str)
# print('s:',y)
# print('---------------------')
# y = re.findall('\S',str)
# print('S:',y)
# print('---------------------')
# y = re.findall('.',str)
# print('.:',y)

# txt = 'my official email is 107.gayathri@gmail.com my personal email is rasangikahw@gmail.com'
# # y = re.findall('\w+@gmail.com',txt)
# y = re.findall('\w+a\w+',txt)
# print(y)

txt = 'Python is great final language'
# y = re.search('Python',txt)
# y = re.search('\wython',txt)
# y = re.search('final',txt)
# y = re.search('f\w{4}',txt)
# print(y)
# print(y.group())
# print(y.span())
# print(y.string)

# y = re.split('\s',txt,1)
# print(y)
# y = re.split('g',txt,)
# print(y)

y = re.sub('\s','@',txt,1)
y = re.sub('f\w{4}','first',txt)
print(y)