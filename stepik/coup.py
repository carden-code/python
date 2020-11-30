# The input to the program is a line of text in which the letter "h" occurs at least twice.
# Write a program that returns the original string and reverses the sequence of characters between the first and
# last occurrences of the letter "h".
#
# Input data format
# The input to the program is a line of text.
#
# Output data format
# The program should display the text in accordance with the condition of the problem.
#
# Sample Input 1:
# abch12345h
#
# Sample Output 1:
# abch54321h
string = input()
flip = string[string.index('h') + 1:string.rindex('h')]
print(string.replace(flip, flip[::-1]))
