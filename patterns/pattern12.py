'''
1 - - - - - - - - 1 
1 2 - - - - - - 2 1
1 2 3 - - - - 3 2 1
1 2 3 4 - - 4 3 2 1
1 2 3 4 5 5 4 3 2 1
'''

n = int(input('Enter the number to create the pattern: '))

for row in range(1, n + 1):

    # Left side:
    for column in range(1, row+1):
        print(f'{column} ', end='')

    # Middle part:
    for column in range((2 * n) - 2 * row):
        print('- ', end='')

    # Right side:
    for column in range(row, 0, -1):
        print(f'{column} ', end='')

    print('')