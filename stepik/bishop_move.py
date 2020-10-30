# You are given two different cells of the chessboard.
# Write a program that determines whether the bishop can get from the first cell to the second in one move.
# The program receives as input four numbers from 1 to 8 each, specifying the column number and line number,
# first for the first cell, then for the second cell.
# The program should output "YES" if the bishop moves from the first cell to the second one, or "NO" otherwise.
#
# Input data format
# The input to the program is four numbers from 1 to 8.
#
# Output data format
# The program should display the text in accordance with the condition of the problem.
#
# Note. The chess bishop moves along the diagonals.
a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
if (a1 - b1) == (a2 - b2) or (a1 + b1) == (a2 + b2):
    print('YES')
else:
    print('NO')
