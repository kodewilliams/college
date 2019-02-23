def RoundNumToNearestMultiple(num, n):
    times = num // n
    if (num % n >= n/2):
        times = times + 1
    return (n * times)

print(RoundNumToNearestMultiple(9, 2))
print(RoundNumToNearestMultiple(712, 25))
print(RoundNumToNearestMultiple(713, 25))
print(RoundNumToNearestMultiple(0, 5))
print(RoundNumToNearestMultiple(79, 1))
