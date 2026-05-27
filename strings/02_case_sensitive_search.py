"""
Problem: Check whether the string contains the word "Python".

Rules:
- If the word exists in the string, print "Found"
- Otherwise, print "Not Found"
- The search should be case-sensitive
"""

text = "Hello World, I'm Python"
word = 'Python'

if word in text:
    print(f'{word} was found in the string')

else:
    print(f'{word} was not found in the string')