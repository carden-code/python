# Two squares of a chessboard are given. Write a program that determines whether the specified cells
# are of the same color or not. If they are painted in one color,
# then output the word "YES", and if they are in different colors, then output "NO".
#
# Input data format
# The program receives four numbers from 1 to 8 each, specifying the column number
# and line number, first for the first cell, then for the second cell.
#
# Output data format
# The program should display the text in accordance with the condition of the problem.

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (x1 + y1 + x2 + y2) % 2 == 0:
    print('YES')
else:
    print('NO')
