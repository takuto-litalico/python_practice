sec = int(input("Enter seconds: "))

hour = sec // 3600
minute = (sec - hour * 3600) // 60
seconds = (sec - hour * 3600 - minute * 60)

a_list = [hour, minute, seconds]

def pzero(num):
    num_str = str(num)
    if num < 10:
        num_str = "0" + str(num)
    return num_str

for i,num in enumerate(a_list):
    a_list[i] = pzero(num)

hour, minute, seconds = a_list

print(str(hour) + ":" + str(minute) + ":" + str(seconds))
