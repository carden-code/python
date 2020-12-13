# Write a function is_password_good (password) that takes the password string value password as an argument and
# returns True if the password is strong and False otherwise.
#
# The password is strong if:
#
# its length is at least 8 characters;
# it contains at least one uppercase letter (uppercase);
# it contains at least one lowercase letter (lowercase);
# it contains at least one digit.
def is_password_good(password):
    dig = False
    alp = False
    upp = False
    if len(password) > 7:
        for c in password:
            if c.isdigit():
                dig = True
            elif c in 'abcdefghijklmnopqrstuvwxyz':
                alp = True
            elif c.isupper():
                upp = True
    else:
        return False

    return dig and alp and upp


txt = input()
print(is_password_good(txt))
