# Write a function is_palindrome (text) that takes the string text as an argument and
# returns True if the specified text is a palindrome and False otherwise.
#
# Note 1: A palindrome is a string that reads the same in both directions
#
# Note 2. When checking, consider uppercase and lowercase letters the same, and also ignore spaces and symbols,. ! ? -.
def is_palindrome(text):
    text_list = [c.lower() for c in ''.join(text.split()) if c not in ',.!?-']
    string = ''.join(text_list)
    return string == string[::-1]


txt = input()
print(is_palindrome(txt))
