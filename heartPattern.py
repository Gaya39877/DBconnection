
for i in range(6):
    for j in range(7):
        if i==0 and j%3 != 0:
            print('* ', end='')
        elif i==1 and j%3 ==0:
            print('* ', end='')
        elif i-j ==2:
            print('* ', end='')
        elif i+j ==8:
            print('* ', end='')
        else:
            print('  ', end='')

    print()