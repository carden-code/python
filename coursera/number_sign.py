# In mathematics, the function sign (x) (number sign) is defined like this:
#
# sign (x) = 1 if x> 0,
#
# sign (x) = - 1 if x <0,
#
# sign (x) = 0 if x = 0.
#
# For a given number x, output the value sign (x).
#
# Input format
#
# One integer is entered.
#
# Output format
#
# Print the answer to the problem.
x = int(input())
if x > 0:
    print(1)
elif x < 0:
    print(-1)
else:
    print(0)
