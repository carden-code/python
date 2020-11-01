# Write a program that finds the smallest and largest of the five numbers.
#
# Input data format
# The program is fed five integers, each on a separate line.
#
# Output data format
# The program should display the smallest and largest number with an explanatory inscription.
num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
num_4 = int(input())
num_5 = int(input())
print('Smallest number =', min(num_1, num_2, num_3, num_4, num_5))
print('Largest number =', max(num_1, num_2, num_3, num_4, num_5))
