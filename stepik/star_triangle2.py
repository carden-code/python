# Write a draw_triangle () function that draws a starry right triangle with legs 10 according to the pattern:
#
# *
# **
# ***
# ****
# *****
# ******
# *******
# ********
# *********
# **********
def draw_triangle():
    leg = 10
    sym = '*'
    for i in range(1, leg + 1):
        print(sym * i)


draw_triangle()
