# Write a draw_box () function that draws a 14x10 star rectangle according to the sample:
# **********
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# **********
def draw_box():
    length = 10
    height = 14
    for i in range(height):
        if i == 0 or i == height - 1:
            print('*' * length)
        else:
            print('*' + (' ' * (length - 2)) + '*')


draw_box()
