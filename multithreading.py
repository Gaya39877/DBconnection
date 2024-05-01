# import threading
# from time import sleep
#
# def func1():
#     for i in range(100):
#         print('gamya')
#         sleep(1)
#
# def func2():
#     for i in range(100):
#         print('bawwh')
#         sleep(1)
#
# t1  = threading.Thread(target=func1)
# t2  = threading.Thread(target=func2)
#
# t1.start()
# sleep(0.2)
# t2.start()

from threading import *
from time import sleep
class A(Thread):
    def run(self):
        for i in range(10):
            print('hello', current_thread().getName())
            sleep(1)
class B(Thread):
    def run(self):
        for i in range(10):
            print('world', current_thread().getName())
            sleep(1)

obj1 = A()
obj2 = B()
obj1.start()
sleep(0.2)
obj2.start()
obj1.join()
obj2.join()
print('bye', current_thread().getName())

