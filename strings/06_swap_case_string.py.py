"""
Problem: Convert uppercase letters to lowercase
         and lowercase letters to uppercase.

Rules:
- Spaces and symbols should remain unchanged
- Character order must be preserved
"""

text = "Hello, I'm huge fan of GTA franchise"
new_text = ''

for letter in text:

    # Convert uppercase letters to lowercase
    if 'A' <= letter <= 'Z':
        new_text += letter.lower()

    # Covert lowercase letters to uppercase
    elif 'a' <= letter <= 'z':
        new_text += letter.upper()

    # Keep symbols and spaces unchanged
    else:
        new_text += letter

print(f'{new_text}')