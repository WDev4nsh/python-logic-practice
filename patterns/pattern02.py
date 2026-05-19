''' 
 * 
 * *
 * * *
 * * * *
 * * * * *
'''

n = int(input('Enter the number to create the pattern: '))

for row in range(n):
    for column in range(row + 1):
        print('* ', end='')
    
    print('')