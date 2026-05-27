"""
Problem: Create a new string where every character
         that occurs more than once is replaced with '*'.

Rules:
- Spaces and symbols should also be checked
- Character order must be preserved
- The search should be case-sensitive
"""

text = 'Hello. . . My name Agent 47.'
text_count = {}
new_text = ''

# Count how many times each character appears
for letter in text:

    if letter not in text_count:
        text_count[letter] = 1

    else:
        text_count[letter] += 1

print(text_count)

# Replace duplicates characters with '*'
for letter in text:

    if text_count[letter] > 1:
        new_text += '*'
    
    else:
        new_text += letter

print(new_text)