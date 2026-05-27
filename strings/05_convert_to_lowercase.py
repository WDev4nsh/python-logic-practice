"""
Problem: Convert all characters in the string to lowercase.

Rules:
- Spaces and symbols should remain unchanged
- Character order must be preserved
"""

text = 'Hello World, I like to drink tea.'
new_text = ''

for letter in text:
    new_text += letter.lower()

print(new_text)