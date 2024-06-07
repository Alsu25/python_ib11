def num_digits(number):
    if number == 0:
        return 1
    else:
        return len(str(abs(number)))
