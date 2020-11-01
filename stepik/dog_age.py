# The input to the program is the number nn - the number of dog years.
# Write a program that calculates a dog's age in human years.
#
# Input data format
# The input to the program is a natural number - the number of dog years.
#
# Output data format
# The program should output the dog's age in human years.
#
# Note. During the first two years, the canine year is 10.5 human years.
# Thereafter, each dog year is equal to 4 human years.
age_dog = float(input("Enter the dog's age:"))
age_person = 0
if age_dog <= 2:
    age_person += (10.5 * age_dog)
    print(age_person)
else:
    age_person += 21
    age_person += (age_dog - 2) * 4
    print("Dog age in human years:", age_person)
