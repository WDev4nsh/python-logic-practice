'''
* * * * * *
* * * * * *
* * * * * *
* * * * * *
* * * * * *
'''

rows = int(input('Enter the number of rows: '))
columns = int(input('Enter the number of columns: '))

for row in range(rows):                 # Controls for rows
    for column in range(columns):             # Controls for columns
        print('* ', end='')

    print('')