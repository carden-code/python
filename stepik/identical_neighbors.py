string = input()
count = 0
for c in range(len(string)):
    if c == len(string) - 1:
        break
    if string[c] == string[c + 1]:
        count += 1
    if c == len(string) - 1:
        break
print(count)
