# In the Windows operating system, the full file name consists of a drive letter,
# after which a colon and a "\" character are put, then the subdirectories (folders) in which the file is located
# are listed after the same character, the file name is written at the end (C: \ Windows \ System32 \ calc.exe).
#
# One line with the correct file name in the Windows operating system is fed to the program.
# Write a program that parses a string into parts separated by a "\" character. Print each part on a separate line.
#
# Input data format
# One line is fed to the program.
#
# Output data format
# The program should display the text in accordance with the condition of the problem.
string = input()
print(*string.split('\\'), sep='\n')
