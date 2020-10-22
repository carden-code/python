# Write a program that reads three numbers and counts the number of even numbers.
num1, num2, num3 = int(input('Enter the first number:')), int(input('Second:')), int(input('Last:'))
count = 0
if num1 % 2 == 0:
    count += 1
if num2 % 2 == 0:
    count += 1
if num3 % 2 == 0:
    count += 1
print('Number of even numbers:', count)
