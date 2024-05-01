# x = 'gayathri rasangika'
# print(x.capitalize())
# print(x.upper())
# print(x.lower())
# print(x.replace('san','f'))
# y = (x.split(' '))
# print(y)
#
# z = ' loves '.join(y)
# print(z)

# x = [2,44,12,4,545]
# print(x)
# x.insert(1,77)
# print(x)
# x.append(22)
# print(x)
# x.remove(545)
# print(x)
# x.pop()
# print(x)
# x.sort(reverse=True)
# print(x)

# a,b,*c = [1,2,3,4,56,7,89,7,2]
# print(a)
# print(b)
# print(c)

# import timeit
# list_time = timeit.timeit(stmt="[1,2,3,4,5]")
# tuple_time = timeit.timeit(stmt="(1,2,3,45,6)")
#
# print(list_time*1000)
# print(tuple_time*1000)

# x = {2,3,4,5}
# print(x)
# x.add('d')
# print(x)
# x.update([32,12,'bye'])
# print(x)

# x = {1,2,3,4,5,6,7}
# y = {2,4,6,8,}
#
# print(x & y)
# print(x.intersection(y))
# print(x | y )
# print(x.union(y))

# x = {1:'bawwh',
#      2:'cowwh',
#      3:'cowbaw'}
# print(x)
# print(type(x))
#
# x["third_party"] =('food','pst')
# print(x)
#
# x.pop(3)
# print(x)
#
# print(x.values())
# print(x.keys())
# print(x.items())

# lst = [1,2,3,4,5,6,7,8,9]
# print(lst[1::2])

# sum = 0;
# i = 1;
# while(i<6):
#     number = int(input("enter number: "))
#     sum= sum+number
#     i+=1
# print("sum of numbers:", sum)


# x = {'name':'gayathri',
#      'age':25,
#      'location':'matara'}
#
# for i in x.keys():
#     print(i)
# print('------------------------------------')
# for i in x.values():
#     print(i)
# print('------------------------------------')
# for i in x.items():
#     print(i)
# print('------------------------------------')
# for i,j in x.items():
#     print((i,j))


# for i in range(1,11):
#     if (i==5):
#         break
#     print(i)
# print('----------------------------')
# x=1;
# for x in range(1,11):
#
#     if(x==6):
#         continue
#     print(x)
#
#     x+=1
# def Rect(height,width):
#     perimeter = 2*(height+width)
#     area = height*width
#     print('Perimeter = ', perimeter)
#     print('Area = ',area)
#
# Rect(
#     height = float(input("enter height of the rectangle: ")),
#     width = float(input("enter width of the rectangle:"))
# )


# def student(subject,marks,**friends):
#     print("Subject = ", subject)
#     print("Marks = ", marks)
#     for keys,values in friends.items():
#         print(keys, "=",values)
# student(
#     subject = str(input('enter subject name: ')),
#     marks = float(input('enter marks: ')),
#     friends = str(input('enter friends here: '))
# )




