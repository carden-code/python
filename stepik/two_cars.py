# Two cars are driving towards each other at constant speeds V_1 and V_2 km / h.
# Determine how long the cars will meet if the distance between them is S km.
#
# Input data format
# The program receives three floating point numbers S, V_1, V_2, each on a separate line.
#
# Output data format
# The program should output one number in accordance with the condition of the problem.
s = float(input())
v_1 = float(input())
v_2 = float(input())
finish = s / (v_1 + v_2)
print(finish)
