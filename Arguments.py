def student_info(name, age, grade):
    print(f'My name is{name}. My age is {age}.')
    print(f'I am in grade {grade}')

# positional arguments
# student_info('kamal',20)

# keyword arguments
# student_info(age =20, name="kamal")

# positional and keyword arguments
# student_info('kamal',grade=12,age=20)

# default arguments
# def student_info2(name, age= 20):
#     print(f'my name is {name}. My age is {age}.')
#
# student_info2("amal")

# variable length arguments / tuple
# def total_marks(*args):
#     total = 0
#     for mark in args:
#         total+=mark
#     print(total)
#
# total_marks(78,65)

# key word arguments/dictionary
# def total_marks(**kwargs):
#     for sub, mark in kwargs.items():
#         print(sub,mark)
#
# total_marks(maths=89, science=78, english=90)