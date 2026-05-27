"""
Problem: Create a new string that removes all vowels
         from the original string.

Rules:
- Both uppercase and lowercase vowels should be removed
- Spaces and symbols should remain unchanged
- Character order must be preserved
"""

vowels = 'AEIOUaeiou'
text = 'Hello Agent 47, your new task is... You have to PLAY GTA FOR 8 HOURS STRAIGHT'
new_text = ''

for letter in text:

    # Add character only if it is not a vowel
    if letter not in vowels:
        new_text += letter

print(new_text)