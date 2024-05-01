# syntax errors
# runtime errors
# logical errors

try:
    a = int(input('enter first no: '))
    b = int(input('enter second no: '))
    print(a/b)
except ZeroDivisionError as e:
    print('can not divide by zero', e)
except ValueError as e:
    print('use integers', e)
except Exception as e :
    print("something went wrong")

finally:
    print('bye')