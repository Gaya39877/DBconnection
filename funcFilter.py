
number = [1,2,3,4,5,6,7,8]

# def even_num(x):
#     return(x%2 == 0)


y = list(filter(lambda x: x%2==0, number))
print(y)