'''
----*----
---***---
--*****--
-*******-
*********
'''

n = int(input('Enter the number to create the pattern: '))

for row in range(1, n + 1):

    # left side:
    for column in range(n - row):
        print('-', end='')

    # Middle part:
    for column in range((2 * row) - 1):
        print('*',  end='')

    # Right side:
    for column in range(n - row):
        print('-', end='')

    print('')