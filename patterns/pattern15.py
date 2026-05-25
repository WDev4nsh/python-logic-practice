'''
A B C D E 
A B C D 
A B C 
A B 
A
'''

n = int(input('Enter the number to create the pattern: '))

for row in range(n):
    char = 65
    for column in range(n - row):
        print(f'{chr(char)} ', end='')
        char += 1

    print('')