# Write a function is_valid_triangle (side1, side2, side3) that takes three natural numbers as arguments,
# and returns True if there is a non-degenerate triangle with sides side1, side2, side3, and False otherwise.
def is_valid_triangle(side1, side2, side3):
    if side2 + side3 > side1 and side1 + side2 > side3 and side1 + side3 > side2:
        return True
    else:
        return False


a, b, c = int(input()), int(input()), int(input())
print(is_valid_triangle(a, b, c))
