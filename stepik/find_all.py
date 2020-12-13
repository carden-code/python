# Recall that the string method find ('a') returns the location of the first occurrence of a in a string.
# The problem is that this method does not find the location of all a characters.
#
# Write a function named find_all (target, symbol) that takes two arguments, the string target and the symbol symbol,
# and returns a list containing all the locations of that symbol in the string.
#
# Note 1. If the specified character does not occur in the string, then an empty list should be returned.
def find_all(target, symbol):
    return [c for c in range(len(target)) if target[c] == symbol]


s = input()
char = input()
print(find_all(s, char))
