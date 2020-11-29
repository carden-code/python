# The Caesar Legion, created in the 23rd century on the basis of the Roman Empire,
# does not change ancient traditions and uses the Caesar code. This let them down,
# because this cipher is very simple.
# However, in the post-apocalypse, people are poorly aware of all the subtleties of the pre-war world,
# so scientists from the NKR cannot understand exactly how to decode these messages.
# Write a program to decode this cipher.
#
# Input data format
# The first line contains the number n, (1 <= n <= 25) - the shift,
# the second line gives the encoded message as a string with lowercase Latin letters.
#
# Output data format
# The program should print one line - the decoded message. Note that you need to decode the message, not encode.
shift = int(input())
string = input()

for i in range(len(string)):
    n = ord(string[i]) - shift
    if n < 97:
        n = 122 - (96 - n)
    print(chr(n), end='')
