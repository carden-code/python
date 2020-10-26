number = int(input())
all_minutes = number // 60
seconds = number % 60
hours = (all_minutes // 60) % 24
minutes = all_minutes % 60

if minutes >= 10 and seconds >= 10:
    print(hours, minutes, seconds, sep=':')
elif minutes < 10 and seconds < 10:
    print(hours, '0' + str(minutes), '0' + str(seconds), sep=':')
elif minutes < 10 and seconds > 9:
    print(hours, '0' + str(minutes), seconds, sep=':')
elif minutes > 9 and seconds < 10:
    print(hours, minutes, '0' + str(seconds), sep=':')
