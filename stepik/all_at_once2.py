# Complete the above code to:
#
# Replaced the second element of the list with 17;
# Added numbers 4, 5 and 6 to the end of the list;
# Removed the first element of the list;
# Doubled the list;
# Inserted number 25 at index 3;
# Displayed a list using the print () function.
# numbers = [8, 9, 10, 11]
numbers = [8, 9, 10, 11]
numbers.pop(1)
numbers.insert(1, 17)
numbers += [4, 5, 6]
numbers.pop(0)
numbers *= 2
numbers.insert(3, 25)
print(numbers)
