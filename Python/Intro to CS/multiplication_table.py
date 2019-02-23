def PrintMultiplicationTable(num_1, num_2):
    # Prints the multiplication table for num_1 x num_2

    for a in range(1, num_1 + 1):
        for b in range(1, num_2 + 1):
            print (a, 'x', b, '=', a * b)


PrintMultiplicationTable(2, 4)
print()
PrintMultiplicationTable(3, 1)
