'''
1
23
456
78910
1112131415
'''

n = int(input('Enter the number to create the pattern: '))

num = 1
for row in range(1, n + 1):
    for column in range(row):
        print(f'{num}', end='')
        num += 1

    print('')