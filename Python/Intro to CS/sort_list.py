def SortList(nums):

    n = len(nums)
        
    for a in range(n-1):
        for b in range(n-1-a):
            if nums[b] > nums[b+1]:
                temp = nums[b]
                nums[b] = nums[b+1]
                nums[b+1] = temp
                

    return nums



print(SortList([6, 4, 2, -1]))
print(SortList([6, 3, 9, 2, 3]))
print(SortList([5]))
print(SortList([ ]))
