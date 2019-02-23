def GetSecondLargestNumber(nums):
    # Returns the second largest unique number in nums.

    n = len(nums)
    if n < 2:
        return None
    elif n == 2:
        if nums[0] == nums[1]:
            return None
    else:
        # Sort the list in descending order
        for c in range(n-1):
            for d in range(n-c-1):
                if nums[d] < nums[d+1]:
                    swap = nums[d]
                    nums[d] = nums[d+1]
                    nums[d+1] = swap

        maximum = nums[0]

        for num in nums:
            if num < maximum:
                return num



print(GetSecondLargestNumber([2, 4, 6, 5, 3, 1]))
print(GetSecondLargestNumber([-2, 0, 2]))
print(GetSecondLargestNumber([-2, -2, -2]))
print(GetSecondLargestNumber([-2, -2, -3, -2]))
print(GetSecondLargestNumber([1]))
print(GetSecondLargestNumber([]))
