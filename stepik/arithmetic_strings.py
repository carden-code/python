len_f = len(input())
len_s = len(input())
len_l = len(input())
len_min = 0
len_sec = 0
len_max = 0
if len_f > len_s and len_f > len_l:
    len_max = len_f
elif len_s > len_f and len_s > len_l:
    len_max = len_s
elif len_l > len_f and len_l > len_s:
    len_max = len_l

if len_f < len_s and len_f < len_l:
    len_min = len_f
elif len_s < len_f and len_s < len_l:
    len_min = len_s
elif len_l < len_f and len_l < len_s:
    len_min = len_l

if len_min < len_f < len_max:
    len_sec = len_f
elif len_min < len_s < len_max:
    len_sec = len_s
elif len_min < len_l < len_max:
    len_sec = len_l

d = len_sec - len_min
print(len_f, len_s, len_l)
print(d)
print(len_min)
print(len_sec)
print(len_max)

if len_sec + d == len_max:
    print('YES')
else:
    print('NO')
