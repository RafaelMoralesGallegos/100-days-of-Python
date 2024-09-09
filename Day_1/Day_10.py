def is_leap_year(year):
    # Write your code here.
    # Don't change the function name.
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


is_leap_year(2000)
