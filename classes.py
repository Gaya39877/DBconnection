# class Phone:
#     def say(self,name):
#         self.x = name
#         print("hello " + name)
#
# phone1 = Phone()
# phone1.say("nokia")
# print(phone1.x)
#
# phone2 = Phone()
# phone2.say("samsung")

# init method
# class student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# st1 = student(
#     name = str(input("enter name: ")),
#     age = int(input("enter age: "))
# )
# st2 = student(
#     name = str(input("enter name: ")),
#     age = int(input("enter age: "))
# )
# print(st1.name)
# print(st1.age)
# print(st2.name)
# print(st2.age)

# private variables
# class myclass:
#     x =18
#     __y = 29
#     def disp(self):
#         return self.__y
#
# myObj = myclass()
# print(myObj.disp())

# private methods(encapsulations)
# class myClass:
#     def meth1(self):
#         print("hello")
#         self.__meth2()
#     def __meth2(self):
#         print("world")
#
# myObj = myClass()
# myObj.meth1()

# inheritance(single , multi level, multiple)
# class phone1:
#     def feature1(self):
#         print('camera')
# class phone2:
#     def feature2(self):
#         print('bluetooth')
# class phone3(phone1, phone2):
#     def feature3(self):
#         print('internet')
#
# myObj = phone3()
# myObj.feature1()
# myObj.feature2()
# myObj.feature3()

# super() and method overriding
# class parent:
#     def func1(self):
#         print("hello")
#
# class child(parent):
#     def func2(self):
#         # super().func1()
#         print('welcome')
#     def func1(self):
#         print('hi')
# myObj = child()
# myObj.func1()

class Fruit:
    number_of_items = None
    unit_price = None
    def set_value(self,x,y):
        self.number_of_items = x
        self.unit_price = y


class Apple(Fruit):
    def price(self):
        print('price for Apple ', self.number_of_items* self.unit_price)

class Mango(Fruit):
    def price(self):
        print('price for Mango', self.number_of_items* self.unit_price)

class Grapes(Fruit):
    def price(self):
        print('price for Grapes ', self.number_of_items* self.unit_price)



myObj1 = Apple()
myObj2 = Mango()
myObj3 = Grapes()


myObj1.set_value(
    x=int(input('enter no of Apples: ')),
    y=float(input('enter unit price: '))
)
myObj1.price()
myObj2.set_value(
    x=int(input('enter no of Mangoes: ')),
    y=float(input('enter unit price: '))
)
myObj2.price()
myObj3.set_value(
    x=int(input('enter no of Grapes: ')),
    y=float(input('enter unit price: '))
)
myObj3.price()