'''
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1
'''

n = int(input('Enter the number to create the pattern: '))

for row in range(1, n + 1):
    for column in range(1, row + 1):
        
        # If the sum of row and column is even,
        # print 1
        if (row + column) % 2 == 0:
            start = 1
            print(f'{start} ', end='')

        # Otherwise print 0
        else:
            start = 0
            print(f'{start} ', end='')

    print('')