# i = {1,2,3,4,5}
#
# itr = iter(i)
# while True:
#     try:
#         print(next(itr))
#     except StopIteration:
#         break



# make own iterator
class myit:
    def __init__(self):
        self.y = 2
    def __iter__(self):
        return self
    def __next__(self):
        val = self.y
        self.y+=2
        return val
myObj = myit()
itr = iter(myObj)
print(next(itr))
print(next(itr))
print(next(itr))