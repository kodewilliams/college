def SortByFrequency(my_list):

    counts = {}
    sorted_list = []

    for item in my_list:
        counts[item] = 0
    
    for item in my_list:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    
    while len(counts) > 0:
        maximum = max(counts, key=counts.get)
        for i in range(counts[maximum]):
            sorted_list.append(maximum)
        del counts[maximum]

    return (sorted_list)
