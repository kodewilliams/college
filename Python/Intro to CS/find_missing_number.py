def FindMissingNumber(num_list):

    # Find the minimum and maximum values of the list
    minimum = min(num_list)
    maximum = max(num_list)

    # Check all numbers in list against numbers between min and max
    for num in range(minimum, maximum+1):
        # If number is between min and max but not in list, it is the missing number
        if num not in num_list:
            return num




print(FindMissingNumber([-6, -11, -8, -9, -10]))
print(FindMissingNumber([45, 47]))
