'''
1
2 2
3 3 3 
4 4 4 4
5 5 5 5 5
'''

n = int(input('Enter the number to create the pattern: '))

for row in range(1, n + 1):
    for column in range(row):
        print(f'{row} ', end='')

    print('')

