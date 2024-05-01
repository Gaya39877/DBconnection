#method overriding
# class parent:
#     def func(self):
#         print('gayathri')
#
# class child:
#     def func(self):
#         print('rasangika')
#
# myObj = child()
# print(myObj.func())


# method overloading

class cals:
    def add(self, a=None, b=None, c=None):
        sum = 0
        if a!=None and b!=None and c!=None:
            sum = a+b+c
            print(sum)
        elif a!=None and b!=None:
            sum = a+b
            print(sum)
        else:
            sum = a
            print(sum)

myObj = cals()
myObj.add(7,3,19)