# The chocolate has the form of a rectangle divided into n × m slices.
# The chocolate can be broken into two parts once in a straight line.
# Determine whether it is possible to break off a piece of chocolate from exactly k slices in this way.
#
# Input format
#
# The program receives three numbers as input: n, m, k.
#
# Output format
#
# The program should output one of two words: YES or NO.
n = int(input())
m = int(input())
k = int(input())
if (k % n == 0 and k <= n * (m - 1)) or (k % m == 0 and k <= m * (n - 1)):
    print('YES')
else:
    print('NO')
