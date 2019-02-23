def IsLeapYear(year):
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False

print(IsLeapYear(307))
print(IsLeapYear(2200))
print(IsLeapYear(2000))
print(IsLeapYear(1800))
print(IsLeapYear(3696))
