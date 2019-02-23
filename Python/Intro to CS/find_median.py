num1 = int(input('Enter 1st number: '))
num2 = int(input('Enter 2nd number: '))
num3 = int(input('Enter 3rd number: '))

if num1 > num2:
    if num2 > num3: 
        middle = num2
    elif num1 > num3:
        middle = num3
    else:
        middle =  num1
else:
    if num2 < num3: 
        middle = num2
    elif num1 > num3:
        middle = num1
    else:
        middle = num3

print ('The middle number is', middle)
