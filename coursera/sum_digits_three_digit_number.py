number = int(input())
first = number // 100
second = (number // 10) % 10
last = number % 10
print(first + second + last)
