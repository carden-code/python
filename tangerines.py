# Tangerines
# n schoolchildren share k mandarins equally,
# the non-dividing remainder remains in the basket.
# How many whole tangerines will each student get? How many whole tangerines are left in the basket?
#
# Input data format
# At the entrance to the program, two integers are served:
# the number of students and the number of tangerines, each on a separate line.
#
# Output data format
# The program should display two numbers: the number of tangerines that the students will get and
# the number of tangerines that will remain in the basket, each on a separate line.

number_students = int(input('Please enter the number of students:'))
number_tangerines = int(input('Please enter the amount of tangerines:'))
schoolchildren = number_tangerines // number_students
basket = number_tangerines % number_students
print('Tangerines went to every student:', schoolchildren)
print('The rest of the tangerines in the basket:', basket)
