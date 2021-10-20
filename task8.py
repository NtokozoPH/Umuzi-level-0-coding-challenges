def num_to_time(num):
    hours = num // 60                               # converting a number into hours
    minutes = num % 60                              # converting a number into minutes
    if (hours > 1) and (minutes > 1):
        print(hours,'hours',',',minutes,'minutes')
    elif (hours <= 1) and (minutes <= 1):
        print(hours,'hour',',',minutes,'minute')
    elif (hours > 1) and (minutes <= 1):
        print(hours,'hours',',',minutes,'minute')
    else:
        print(hours,'hour',',',minutes,'minutes')