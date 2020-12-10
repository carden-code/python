# The input to the program is a line of text.
# Write a program that determines if the entered string is a valid phone number.
# A line of text is a valid phone number if it has the format:
#
# abc-def-hijk or
# 7-abc-def-hijk
# where a, b, c, d, e, f, h, i, j, k are numbers from 0 to 9.
#
# Input data format
# The input to the program is a line of text.
#
# Output data format
# The program should print "YES" if the line is a valid phone number and "NO" otherwise.
#
# Note. The phone number must contain only numbers and the symbol -,
# and the number of digits in each group must be correct.
string = input()
arr = [c for c in string.split('-')]
num = ''.join(arr)

if num.isdigit():
    if len(arr) == 3 and len(arr[0]) == 3 and len(arr[1]) == 3 and len(arr[2]) == 4:
        print('YES')
    elif len(arr) == 4 and arr[0] == '7' and len(arr[1]) == 3 and len(arr[2]) == 3 and len(arr[3]):
        print('YES')
    else:
        print('NO')
else:
    print('NO')
