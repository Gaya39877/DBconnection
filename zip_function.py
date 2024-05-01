names = ['gayathri','rasangika','bikki','bawwh']
age = [25,26,27,28]

details = list(zip(names,age))
print(details)
# details = tuple(zip(names,age))
# print(details)
# details = set(zip(names,age))
# print(details)
# details = dict(zip(names,age))
# print(details)

unzip = list(zip(*details))
print(unzip)