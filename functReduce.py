from functools import reduce

number = [1,2,3,4,5,6,7,8]

sum = reduce(lambda x,y: x+y, number)

print(sum)