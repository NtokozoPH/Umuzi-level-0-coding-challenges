def maximum(*numbers):
    max_num = 0            # initialising a maximum number
    for num in numbers:
        if num > max_num:  # checking if current number is greater than current maximum number
            max_num = num  # updating maximum number if less the current number
    return max_num    