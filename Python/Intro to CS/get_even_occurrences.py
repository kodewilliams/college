def GetEvenNumOccurrences(values):
    counts = {}
    evens = []
    
    # Initialize value counts as 0
    for item in values:
        counts[item] = 0

    # Count the occurrences of each value
    for value in counts:
        for num in values:
            if num == value:
                counts[value] += 1

    # Add value to list if the count is divisible by 2
    for key in counts:
        if counts[key] % 2 == 0:
            evens.append(key)
            
    return evens
