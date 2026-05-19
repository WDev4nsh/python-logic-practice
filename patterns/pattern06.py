'''
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
'''

n = int(input('Enter the number to create the pattern: '))

for row in range(n):
    for column in range(1, (n + 1) - row):
        print(f'{column} ', end='')
    
    print('')