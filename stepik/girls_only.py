# The football team recruits girls from 10 to 15 years old inclusive.
# Write a program that asks for the age and gender of an applicant,
# using the gender designation m (for male) and f (for female) to determine whether the applicant is eligible to join
# the team or not. If the applicant fits, then output "YES", otherwise output "NO".
#
# Input data format
# At the entrance to the program, a natural number is submitted - the age of the applicant and
# the letter denoting the sex m (man) or f (woman).
#
# Output data format
# The program should display the text in accordance with the condition of the problem.
age = int(input('Enter your age:'))
sex = input('Enter your gender ( m - man or f - woman ):')
if 10 <= age <= 15 and sex == 'f':
    print('YES')
else:
    print('NO')
