# BEEGEEK finally opened its own bank, which uses special ATMs with an unusual password.
#
# A valid BEEGEEK bank password is a: b: c, where a, b and c are natural numbers.
# Since the founder of BEEGEEK is a fan of mathematics, he decided:
#
# number a - must be a palindrome;
# number b - must be simple;
# number c - must be even.
# Write a function is_valid_password (password) that takes the password string value password as an argument
# and returns True if the password is a valid bank BEEGEEK password and False otherwise.
def is_prime(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False


def is_valid_password(password):
    l_psw = password.split(':')
    return len(l_psw) == 3 and l_psw[0] == l_psw[0][::-1] and is_prime(int(l_psw[1])) and int(l_psw[2]) % 2 == 0


psw = input()

print(is_valid_password(psw))
