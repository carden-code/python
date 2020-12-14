# Write a function get_middle_point (x1, y1, x2, y2) that takes the coordinates of the ends of the segment as arguments
# (x1; y1) and (x2; y2) and returns the coordinates of the point that is the midpoint of the given segment.
def get_middle_point(x1, y1, x2, y2):
    return (x1 + x2) / 2, (y1 + y2) / 2


# считываем данные
x_1, y_1 = int(input()), int(input())
x_2, y_2 = int(input()), int(input())

# вызываем функцию
x, y = get_middle_point(x_1, y_1, x_2, y_2)
print(x, y)
