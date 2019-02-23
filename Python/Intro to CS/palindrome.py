def IsPalindrome(values):
    values_copy = values
    n = len(values)
    matches = 0
    i = 0
    
    for i in range(n):
        if values[i] == values_copy[n-1-i]:
            matches += 1

    if matches == len(values):
        return True
    else:
        return False


print(IsPalindrome([-10, -1, -1, -10]))
print(IsPalindrome(['pizza', 14, 'corn', 14, 'pizza']))
print(IsPalindrome(['pizza', 'pie', 'corn', 'pizza']))
print(IsPalindrome([10]))
