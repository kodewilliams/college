def CombineTwoSortedLists(list1, list2):
    # If either list is empty, return the other one
    if len(list1) == 0:
        return list2
    elif len(list2) == 0:
        return list1
    else:
        # If lists aren't empty, append them to each other
        sorted_list = list1 + list2
        # Sort lists
        for x in range(len(sorted_list)-1, 0, -1):
            for y in range(x):
                if sorted_list[y] > sorted_list[y+1]:
                    temp = sorted_list[y]
                    sorted_list[y] = sorted_list[y+1]
                    sorted_list[y+1] = temp
        return sorted_list

