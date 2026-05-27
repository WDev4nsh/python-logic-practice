"""
Problem: Check whether the string contains the word "Python".

Rules:
- If the word exists in the string, print "Found"
- Otherwise, print "Not Found"
- The search should be case-sensitive
"""

text = "Hello World, I'm python"
word = 'Python'

if word.lower() in text.lower():
    print(f'{word} was found in the string')

else:
    print(f'{word} was not found in the string')