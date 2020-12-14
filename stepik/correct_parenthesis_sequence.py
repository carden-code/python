# Write the is_correct_bracket (text) function that takes a non-empty string text consisting of the characters "()"
# as an argument and returns True if the input string is a valid parenthesis sequence and False otherwise.
#
# Note 1. A regular parenthesis sequence is a string consisting only of characters "()",
# where each open parenthesis has a matching closing parenthesis.
def is_correct_bracket(text):
    if text.count('(') != text.count(')') or text[0] == ')' or text[-1] == '(':
        return False
    string = text.replace('()', '')
    while len(string) != 0:
        if string == ')(':
            return False
        string = string.replace('()', '')
    return string == ''


txt = input()
print(is_correct_bracket(txt))
