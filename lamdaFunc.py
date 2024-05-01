
# area = lambda x, y : x*y
#
# print(area(5,4))

def apple(unit_price):
    return(lambda number_of_apples : number_of_apples*unit_price)

x = apple(40)
print(x(8))