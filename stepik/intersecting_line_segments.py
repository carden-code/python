# There are two segments on the number line: [a1, b1] and [a2, b2]. Write a program that finds their intersection.
# The intersection of two segments can be:
# - section;
# - dot;
# - empty set;
#
# Input data format
# The program receives 4 integers a1, b1, a2, b2, each on a separate line.
# It is guaranteed that a1 <b1 and a2 <b2.
#
# Output data format
# The program should display the boundaries of the segment that is the intersection,
# either a common point or the text "empty set".

a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
if a1 == a2 and b1 == b2:
    print(a1, b1)
elif a1 < b1 == a2 < b2:
    print(b1)
elif a2 < b2 == a1 < b1:
    print(b2)
elif not a1 > a2 and a2 < b1:
    if b2 > b1:
        print(a2, b1)
    else:
        print(a2, b2)
elif not a1 <= a2 and a1 < b2:
    if b2 < b1:
        print(a1, b2)
    else:
        print(a1, b1)
else:
    print('empty set')
