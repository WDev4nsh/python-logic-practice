'''
*
**
***
****
*****
****
***
**
*
'''

n = int(input('Enter the number to create the pattern: '))

# Total rows become 9 when n = 5
for row in range(1, 2 * n):             

    star = row

    # When row becomes greater than n,
    # start decreasing the stars
    if star > n:
        star = 2 * n - row    

    # Otherwise print normal increasing triangle
    else:
        star = row   

    # Print stars according to star variable
    for column in range(star):
        print('*', end='')

    print('')