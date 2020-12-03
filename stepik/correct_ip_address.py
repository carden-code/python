# The input to the program is a line of text containing 4 integers separated by a dot.
# Write a program that determines if the entered line of text is a valid ip address.
#
# Input data format
# The input to the program is a line of text containing 4 integers separated by a dot.
#
# Output data format
# The program should print "YES" if the entered string is a valid ip-address, and "NO" otherwise.
#
# Note. The ip-address is correct if all 4 numbers are in the range from 0 to 255, inclusive.
string_ip = input()
list_ip = string_ip.split('.')
flag = True
for i in list_ip:
    if int(i) not in range(0, 256):
        flag = False
        break

print('YES' if flag else 'NO')
