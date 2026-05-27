"""
Problem: Create a new string where every character
         that occurs more than once is replaced with '*'.

Rules:
- The search should be case-insensitive
- Spaces and symbols should also be checked
- Character order must be preserved
"""

text = 'Hello. . . My name Agent 47.'
text_count = {}
new_text = ''

# Count how many times each character appears
for letter in text:

    # Convert character to lowercase
    # before storing in dictionary
    if letter.lower() not in text_count:
        text_count[letter.lower()] = 1

    else:
        text_count[letter.lower()] += 1
    
print(text_count)

# Add only unique characters to the new string
for letter in text:

    if text_count[letter.lower()] > 1:
        new_text += '*'

    else:
        new_text += letter

print(new_text)