'''
A
A B
A B C
A B C D
A B C D E
'''

n = int(input('Enter the number to create the pattern: '))

for row in range(1, n + 1):
    char = 65
    for column in range(row):
        print(f'{chr(char)} ', end='')
        char += 1

    print('')