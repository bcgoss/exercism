def is_leap_year(arg):
    return arg % 4 == 0 and arg % 100 != 0 or arg % 400 == 0
