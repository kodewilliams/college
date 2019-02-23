def PrintMultiples(start, end, multiple):

    if (multiple == 0):
        print ('Input multiple must be greater than 0')
        return

    if (start >= end):
        temp = start
        start = end
        end = temp
        
    multiples = []
    
    for i in range(start, end + 1):
        if (i % multiple == 0):
            multiples = multiples + [i]
    if (len(multiples) == 0):
        print ('There are no multiples of', multiple, 'in the range of', start, 'to', end)
    else:
        for n in multiples:
            print (n)
        


PrintMultiples(4, 10, 2)
print('')
PrintMultiples(7, -7, 3)
print('')
PrintMultiples(7, 10, 6)
print('')
PrintMultiples(-6, -6, 1)
print('')
PrintMultiples(1, 5, 0)
print('')
