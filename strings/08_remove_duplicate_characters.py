"""
Problem: Create a new string that keeps only the
         characters that appear once in the string.

Rules:
- Duplicate characters should be removed
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

# Add only unique characters to the new string
for letter in text:

    if text_count[letter] == 1:
        new_text += letter

print(new_text)