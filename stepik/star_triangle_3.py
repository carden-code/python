# Write a draw_triangle () function that outputs a star-shaped isosceles triangle with base and
# height 15 and 8, respectively:
#
# Note 1. Use a for loop to display the triangle.
#
# Note 2. There are no spaces to the right of the asterisks.
def draw_triangle():
    height = 12
    base = 55
    sym = '*'
    base_0_5 = base // 2
    sym_print = sym
    for _ in range(height):
        print(' ' * base_0_5 + sym_print)
        base_0_5 -= 1
        sym_print += sym * 2


draw_triangle()
