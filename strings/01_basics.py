"""
Basics Foundation Of Strings
"""

# ===== STRING CREATION =====
text = 'Hello'
text2 = " Python "
text3 = '''I Love Peace, Dev'''

# ===== STRING INDEXING =====
print(text[1])
print(text[-1])

# ===== STRING SLICING =====
# [start : stop : step]
print(text[0:3])
print(text[:4])
print(text[2:])
print(text[::-1])    # Reverse string

# ===== STRING LENGTH =====
print(len(text))

# ===== STRING TRAVERSING =====
for char in text:
    print(char)

for char in range(len(text)):
    print(text[char])

# ===== STRING CONCATENATION =====
print(text + ' ' + text2)

# ===== STRING REPETITION =====
print('Yoo' * 3)
print(text2 * 3)

# ===== STRING MEMBERSHIP =====
print('A' in text)          # False: A is not present in text
print('A' not in text)      # True: A is not present in text

# ===== OTHER METHODS =====

# ----- CASE METHODS -----
print(text.upper())
print(text.lower())
print(text.title())          # Makes first LETTER of EVERY word Capital
print(text.capitalize())     # Makes first character uppercase 
print(text.swapcase())       # Swaps uppercase to lowercase and vice versa

# ----- REMOVING SPACES -----
print(text2.strip())
print(text2.lstrip())            # Remove space from left
print(text2.rstrip())            # Remove space from right

# ----- SEARCHING METHODS -----
print(text.find('H'))            # Returns Index position of character
print(text.index('e'))           # Same as find() but raises error if character is not found
print(text.count('e'))
print(text.startswith('He'))     # Return True or False if string starts with something
print(text.endswith('O'))        # Return True or False if string ends with something

# ----- REPLACING / SPLITTING METHODS -----
print(text.replace('H', 'h'))
print(text.replace('l', 'L', 1)) # Replace only one value

print(text3.split())             # Convert one string into many pieces (List)   
print(text3.split(', '))         # Split using special Character

words = ['I', 'Love', 'Peace,', 'Dev']
print(' '.join(words))           # Opposite of split()

# ----- CHECKING METHODS -----
print(text.isalpha())            # Return True or False if all char is alphabets only
print(text.isdigit())            # Checks if all char are digits
print(text.isalnum())            # Checks if string contains only alphabets and numbers
print(text.isspace())            # Checks if string ONLY contain space
print(text.islower())            
print(text.isupper())

# ----- ESCAPE CHARS -----
print('Hello \n World')         # Prints new line
print('Hello \t World')         # Prints tab spacing
print("Hello \"World\"")        # Prints double quotes
print('Hello\\World')           # Prints Backlash

# ----- FORMATTING -----
print(f'Hello {text2}')
print('Hello {}'.format(text2))

# ----- ASCII BASICS -----
print(ord('A'))                 # Print ASCII value of 'A'
print(ord('a'))
print(chr(65))                  # Returns character from ASCII value