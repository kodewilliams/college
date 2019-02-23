def GetDayOfYear(month, day):
    jan = mar = may = jul = aug = octo = dec = 31
    feb = 28
    apr = jun = sep = nov = 30
    if (month == "january"):
        return day
    elif (month == "february"):
        return (jan + day)
    elif (month == "march"): 
        return (jan + feb + day)
    elif (month == "april"):
        return (jan + feb + mar + day)
    elif (month == "may"):
        return (jan + feb + mar + apr + day)
    elif (month == "june"):
        return (jan + feb + mar + apr + may + day)
    elif (month == "july"):
        return (jan + feb + mar + apr + may + jun + day)
    elif (month == "august"):
        return (jan + feb + mar + apr + may + jun + jul + day)
    elif (month == "september"):
        return (jan + feb + mar + apr + may + jun + jul + aug + day)
    elif (month == "october"):
        return (jan + feb + mar + apr + may + jun + jul + aug + sep + day)
    elif (month == "november"):
        return (jan + feb + mar + apr + may + jun + jul + aug + sep + octo + day)
    elif (month == "december"):
        return (jan + feb + mar + apr + may + jun + jul + aug + sep + octo + nov + day)


print(GetDayOfYear('january', 1))
print(GetDayOfYear('may', 5))
print(GetDayOfYear('december', 18))
