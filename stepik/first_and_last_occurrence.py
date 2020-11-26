# The input to the program is a line of text.
# If this line contains the letter "f" only once, print its index.
# If it occurs two or more times, print the index of its first and last occurrences on one line,
# separated by a space character. If the letter "f" does not appear in this line, print "NO".
#
# Input data format
# The input to the program is a line of text.
#
# Output data format
# The program should display the text in accordance with the condition of the problem.
string = input()
if string.count('f') == 1:
    print(string.find('f'))
elif string.count('f') > 1:
    print(string.find('f'), string.rfind('f'))
else:
    print('NO')
