'''
* * * * *
* * * *
* * *
* *
*
'''

n = int(input('Enter the number to create the pattern: '))

for row in range(n):
    for column in range(n - row):
        print('* ', end='')

    print('')