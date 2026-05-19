'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''

n = int(input('Enter the number to create the pattern: '))

for row in range(1, n + 1):
    for column in range(1, row + 1):
        print(f'{column} ', end='')

    print('')