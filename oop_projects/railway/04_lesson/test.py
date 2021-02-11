li = input()
if len(li) in [5, 6]:
    if li[:3].isalnum():
        if li[3:4] == '-' and li[4:].isalnum():
            print('Yes')
        elif li[3:].isalnum():
            print('Yes')
        else:
            print('NO')
    else:
        print('NO')
else:
    print('NO')
