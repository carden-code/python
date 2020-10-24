# You are given two different cells of the chessboard.
# Write a program that determines if the king can get from the first square to the second in one move.
# The program receives as input four numbers from 1 to 8 each, specifying the column number and line number,
# first for the first cell, then for the second cell.
# The program should print "YES" if you can get to the second one from the first square by the king's move,
# or "NO" otherwise.
#
# Input data format
# The program receives four numbers from 1 to 8.
#
# Output data format
# The program should display the text in accordance with the condition of the problem.
#
# Note. The chess king moves horizontally, vertically and diagonally, but only 1 square.
x_1 = int(input())
y_1 = int(input())
x_2 = int(input())
y_2 = int(input())
if x_1 == x_2 and y_1 == y_2:
    print('YES')
elif (x_1 == (x_2 - 1) or x_1 == (x_2 + 1)) and (y_1 == (y_2 - 1) or y_1 == (y_2 + 1)):
    print('YES')
elif (x_1 == (x_2 - 1) or x_1 == (x_2 + 1)) and y_1 == y_2:
    print('YES')
elif x_1 == x_2 and (y_1 == (y_2 - 1) or y_1 == (y_2 + 1)):
    print('YES')
else:
    print('NO')
