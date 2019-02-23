def GetSecondLargestNumber(nums, n):
    # Returns the nth largest unique number in nums.
    
    l = len(nums)
    if l < 2:
        return None
    elif l == 2:
        if nums[0] == nums[1]:
            return None
    elif n > l:
        return None
    else:
        # Sort the list in descending order
        for c in range(l-1):
            for d in range(l-c-1):
                if nums[d] < nums[d+1]:
                    swap = nums[d]
                    nums[d] = nums[d+1]
                    nums[d+1] = swap

        # Loop through list to determine nth largest #
        target = nums[0]
        count = 1
        for x in range(1, l):
            if count == n:
                return target
            else:
                if nums[x] < target:
                    target = nums[x]
                    count += 1
                elif nums[x] == target:
                    continue
        
            

print(GetSecondLargestNumber([2, 4, 6, 5, 3, 1, 5, 4], 1))
print(GetSecondLargestNumber([2, 4, 6, 5, 3, 1, 5, 4], 2))
print(GetSecondLargestNumber([2, 4, 6, 5, 3, 1, 5, 4], 3))
print(GetSecondLargestNumber([2, 4, 6, 5, 3, 1, 5, 4], 10))
print(GetSecondLargestNumber([], 1))
