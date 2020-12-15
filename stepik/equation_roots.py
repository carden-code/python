# Write a function solve (a, b, c) that takes three integers a, b, c as arguments - the coefficients
# of the quadratic equation a * x ** 2 + b * x + c = 0 and returns its roots in ascending order.
def solve(a, b, c):
    d = b ** 2 - 4 * a * c
    x_1 = (-b + d ** 0.5) / (2 * a)
    x_2 = (-b - d ** 0.5) / (2 * a)
    return sorted((x_1, x_2))


a, b, c = int(input()), int(input()), int(input())

x1, x2 = solve(a, b, c)
print(x1, x2)
