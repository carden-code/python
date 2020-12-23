error = 0
arr = ["\t___________", "\t|/        |", "\t|", "\t|", "\t|", "\t|", "\t|__________"]
for c in range(len(arr)):
    if error < 6:
        arr[2] = "\t|         O"
    if error < 5:
        arr[3] = "\t|         |"
    if error < 4:
        arr[3] = "\t|        /|"
    if error < 3:
        arr[3] = "\t|        /|\\"
    if error < 2:
        arr[4] = "\t|        / "
    if error < 1:
        arr[4] = "\t|        / \\"
    else:
        print(arr[c])

# for c in arr:
#     print(c)
a = '___________'
b = '||||||'
# print(a)
# for c in range(len(b)):
#     if error == 6:
#         if c == 0:
#             print(b[c] + '/' + '        |')
#         elif c == 5:
#             print(b[c] + '__________')
#         else:
#             print(b[c])
#     elif error == 5:



# if error == 6:
#     print("\t___________")
#     print("\t|/        |")
#     print("\t|")
#     print("\t|")
#     print("\t|")
#     print("\t|")
#     print("\t|__________")
# if error == 5:
#     print("\t___________")
#     print("\t|/        |")
#     print("\t|         O")
#     print("\t|")
#     print("\t|")
#     print("\t|")
#     print("\t|__________")
# if error == 4:
#     print("\t___________")
#     print("\t|/        |")
#     print("\t|         O")
#     print("\t|         |")
#     print("\t|")
#     print("\t|")
#     print("\t|__________")
# if error == 3:
#     print("\t___________")
#     print("\t|/        |")
#     print("\t|         O")
#     print("\t|        /|")
#     print("\t|")
#     print("\t|")
#     print("\t|__________")
# if error == 2:
#     print("\t___________")
#     print("\t|/        |")
#     print("\t|         O")
#     print("\t|        /|\\")
#     print("\t|")
#     print("\t|")
#     print("\t|__________")
# if error == 1:
#     print("\t___________")
#     print("\t|/        |")
#     print("\t|         O")
#     print("\t|        /|\\")
#     print("\t|        / ")
#     print("\t|")
#     print("\t|__________")
# if error == 0:
#     print("\t___________")
#     print("\t|/        |")
#     print("\t|         O")
#     print("\t|        /|\\")
#     print("\t|        / \\")
#     print("\t|")
#     print("\t|__________")
