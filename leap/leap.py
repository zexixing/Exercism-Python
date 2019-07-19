def is_leap_year(year):
    flag = 0
    if isinstance(year,int) or isinstance(year,float):
        if year%4.0 == 0:
            if year%100.0 != 0:
                flag = 1
            elif year%400.0 == 0:
                flag = 1
    return bool(flag)
