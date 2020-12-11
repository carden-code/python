# Write a draw_triangle (fill, base) function that takes two parameters:
#
# fill - placeholder character;
# base - the size of the base of an isosceles triangle;
# and then outputs it.
#
# Note. It is guaranteed that the base of the triangle is odd.
def draw_triangle(fill, base):
    for i in range((base // 2) + 1):
        for _ in range(i + 1):
            print(fill, end='')
        print()
    for i in range((base // 2), 0, -1):
        for _ in range(i):
            print(fill, end='')
        print()


draw_triangle(input(), int(input()))
