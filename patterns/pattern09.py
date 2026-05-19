'''
----*----     
---***---
--*****--
-*******-
*********
*********
-*******-
--*****--
---***---
----*----
'''

n = int(input('Enter the number to create the pattern: '))

# Upper triangle
for row in range(1, n + 1):

    # left side:
    for column in range(n - row):
        print('-', end='')
    
    # Middle part:
    for column in range(2 * row - 1):
        print('*', end='')

    # Right side:
    for column in range(n - row):
        print('-', end='')
    
    print('')

# Lower triangle
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