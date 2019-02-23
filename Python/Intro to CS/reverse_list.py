def ReverseList(items):
    newList = []
    for i in range(len(items)):
        newList.append(items.pop())

    return newList


print(ReverseList([1, 2, 3, 4]))
print(ReverseList(['hi', 1, 'seven', 3, 2]))
print(ReverseList([5]))
print(ReverseList([ ]))
