'''
*********
-*******-
--*****--
---***---
----*----
'''

n = int(input('Enter the number to create the pattern: '))

for row in range(n):

    # Left side:
    for column in range(row):
        print('-', end='')

    # Middle part:
    for column in range((2 * n - 1) - 2 * row):
        print('*', end='')

    # Right side:
    for column in range(row):
        print('-', end='')

    print('')