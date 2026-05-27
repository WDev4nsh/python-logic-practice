"""
Problem: Create a new string where every repeated
         alphabet character is replaced with '*'.

Rules:
- The search should be case-sensitive
- Spaces and symbols should remain unchanged
- Only alphabet characters should be checked
- Character order must be preserved
"""

text = 'Hello... My name is Agent 47.'
text_count = {}
new_text = ''

# Count how many times each alphabet character appears
for letter in text:

    if 'A' <= letter <= 'Z' or 'a' <= letter <= 'z':

        if letter not in text_count:
            text_count[letter] = 1

        else:
            text_count[letter] += 1

# Replace repeated alphabet characters with '*'
for letter in text:

    if 'A' <= letter <= 'Z' or 'a' <= letter <= 'z':

        if text_count[letter] > 1:
            new_text += '*'

        else:
            new_text += letter

    # Keep symbols and spaces unchanged
    else:
        new_text += letter

print(new_text)