"""
Problem: Create a new string that contains only the first occurrence
         of each character from the original string.

Rules:
- The search should be case-sensitive
- Spaces and symbols should be included
- Character order must be preserved
"""

text = 'Hello python, My name is World'
new_text = ''

for letter in text:
    
    # Add character only if it does not
    # already exist in the new string
    if letter not in new_text:
        new_text += letter

print(f'{new_text}')