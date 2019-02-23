def GetNextDate(month, day, year):
    if (month == 2):
        if (day < 28):
            day += 1
        else:
            day = 1
            month += 1
    elif (month == 1 or month == 3 or month == 5 or month == 7 or
          month == 8 or month == 10 or month == 12):
        if (day < 31):
            day += 1
        elif (month == 12 and day == 31):
            day = 1
            year += 1
            month = 1
        else:
            day = 1
            month += 1
    elif (month == 4 or month == 6 or month == 9 or month == 11):
        if (day < 30):
            day += 1
        else:
            day = 1
            month += 1

    return str(month) + '/' + str(day) + '/' + str(year)
    


print(GetNextDate(9, 16, 2016))
print(GetNextDate(12, 31, 2016))
print(GetNextDate(2, 28, 2004))
