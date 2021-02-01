normal_to_sleep = int(input()) #time sleeping
hour = int(input())            #hour going to sleep
minutes = int(input())          #minut going to sleep
all_time = (normal_to_sleep + (hour * 60) + minutes)
print((all_time // 60), (all_time % 60), sep="\n")

