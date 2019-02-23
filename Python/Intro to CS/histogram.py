def PrintHistogram(nums):

    checked = []
    
    for num in nums:
        found = 'F'
        for item in checked:
            if item == num:
                found = 'T'
                
        if found == 'T':
            continue
        
        checked += [num]
        c = 0
        for i in range(len(nums)):
            if num == nums[i]:
                c += 1
            
        print (num, ':', end=' ')
        for x in range(c):
            print ('*', end='')
            
        print()



PrintHistogram([-2, -2, -3, -2])
print()
PrintHistogram([1, 2.5, 3, 4, 4, 3, 6])
print()
PrintHistogram([4, 7, 3, 7, 9, 3, 3])
