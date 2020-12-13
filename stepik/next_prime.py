# Write a function get_next_prime (num) that takes a natural number num as an argument
# and returns the first prime number greater than num.
#
# Note 1. Use the is_prime () function from the previous task.
def is_prime(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False


def get_next_prime(num):
    num += 1
    while not is_prime(num):
        num += 1
    return num


n = int(input())

# вызываем функцию
print(get_next_prime(n))
