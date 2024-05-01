# n = int(input('enter number: '))
# for i in range(n):
#     for j in range(i+1):
#         print('*', end='')
#     print()
#
# m = int(input('enter number: '))
# for i in range(m):
#     for j in range(m-i):
#         print("*", end='')
#     print()

m = int(input('enter number: '))
for i in range(m):
    for j in range(m-i-1):
        print(" ", end='')
    for k in range(2*i+1):
        print("*", end='')
    print()