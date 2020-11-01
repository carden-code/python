# The famous American writer Ray Bradbury has a novel called Fahrenheit 451.
# Write a program that determines which temperature in Celsius corresponds to a specified value in Fahrenheit.
# Input data format
# A real number of degrees Fahrenheit is fed to the input of the program.
#
# Output data format
# The program should output the number of degrees in Celsius.
f = float(input())
c = (5 / 9) * (f - 32)
print(c)
