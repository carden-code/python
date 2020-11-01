num = int(input())
first_digit = num // 100
second_digit = num % 100 // 10
last_digit = num % 10
first = max(first_digit, last_digit, second_digit)
last = min(first_digit, last_digit, second_digit)
second = 0
if (first_digit == first and second_digit == last) or (second_digit == first and first_digit == last):
    second = last_digit
elif (first_digit == first and last_digit == last) or (last_digit == first and first_digit == last):
    second = second_digit
elif (second_digit == first and last_digit == last) or (second_digit == last and last_digit == first):
    second = first_digit
if first - last == second:
    print('Число интересное')
else:
    print('Число неинтересное')
