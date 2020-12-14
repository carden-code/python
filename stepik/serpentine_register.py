# Write a function convert_to_python_case (text) that takes a camel-case string
# as an argument and converts it to snake-case.
def convert_to_python_case(text):
    list_text = [c for c in ''.join(text.split())]
    python_case = []
    for c in range(len(list_text)):
        if list_text[c] == list_text[c].upper() and not list_text[c].isdigit():
            python_case.append('_' + list_text[c])
        else:
            python_case.append(list_text[c])
    return ''.join(python_case).lower()[1:]


txt = input()
print(convert_to_python_case(txt))
