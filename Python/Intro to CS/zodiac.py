
def GetZodiacSign(birth_month, birth_day):
    if ((birth_month == "march" and birth_day >= 21) or (birth_month == "april" and birth_day <= 19)):
        sign = "aries"
    elif ((birth_month == "april" and birth_day >= 20) or (birth_month == "may" and birth_day <= 20)):
        sign = "taurus"
    elif ((birth_month == "may" and birth_day >= 21) or (birth_month == "june" and birth_day <= 20)):
        sign = "gemini"
    elif ((birth_month == "june" and birth_day >= 21) or (birth_month == "july" and birth_day <= 22)):
        sign = "cancer"
    elif ((birth_month == "july" and birth_day >= 23) or (birth_month == "august" and birth_day <= 22)):
        sign = "leo"
    elif ((birth_month == "august" and birth_day >= 23) or (birth_month == "september" and birth_day <= 22)):
        sign = "virgo"
    elif ((birth_month == "september" and birth_day >= 23) or (birth_month == "october" and birth_day <= 22)):
        sign = "libra"
    elif ((birth_month == "october" and birth_day >= 23) or (birth_month == "november" and birth_day <= 21)):
        sign = "scorpio"
    elif ((birth_month == "november" and birth_day >= 22) or (birth_month == "december" and birth_day <= 21)):
        sign = "sagittarius"
    elif ((birth_month == "december" and birth_day >= 22) or (birth_month == "january" and birth_day <= 19)):
        sign = "capricorn"
    elif ((birth_month == "january" and birth_day >= 20) or (birth_month == "february" and birth_day <= 18)):
        sign = "aquarius"
    elif ((birth_month == "february" and birth_day >= 19) or (birth_month == "march" and birth_day <= 20)):
        sign = "pisces"

    return sign


print(GetZodiacSign("march", 15))
print(GetZodiacSign("july", 21))
print(GetZodiacSign("february", 14))
