sec = int(input("Enter seconds: "))

hour = sec // 3600
minute = (sec - hour * 3600) // 60
seconds = (sec - hour * 3600 - minute * 60)

a_list = [hour, minute, seconds]

def pzero(a):
    if a <= 10:
        pa = "0" + str(a)
    else:
        pass
    return pa

for i in a_list:
    i = pzero(i)

print(str(hour) + ":" + str(minute) + ":" + str(seconds))
