# The chess king moves horizontally, vertically and diagonally, but only 1 square.
# Given two different squares of the chessboard,
# determine if the king can get from the first square to the second in one move.
#
# Input format
#
# The program receives as input four numbers from 1 to 8 each,
# specifying the column number and line number, first for the first cell, then for the second cell.
#
# Output format
#
# The program should output YES if it is possible to get to the second one from the first cell by the king's move,
# or NO otherwise.

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 == x2 and y1 == y2:
    print('YES')
elif x1 == x2 and (y1 == (y2 + 1) or y1 == (y2 - 1)):
    print('YES')
elif (x1 == (x2 + 1) or x1 == (x2 - 1)) and y1 == y2:
    print('YES')
elif (x1 == (x2 + 1) or x1 == (x2 - 1)) and (y1 == (y2 + 1) or y1 == (y2 - 1)):
    print('YES')
else:
    print('NO')
