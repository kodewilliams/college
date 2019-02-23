'''
You need to complete the code in the following functions:
- SubtractNumbers
- MultiplyNumbers
- DivideNumbers
'''

def AddNumbers(num_1, num_2):
    '''
    This function should return num_1 + num_2.
    '''
    return num_1 + num_2


def SubtractNumbers(num_1, num_2):
    '''
    This function should return num_1 - num_2. Replace the line below with the
    correct code.
    '''
    return num_1 - num_2


def MultiplyNumbers(num_1, num_2):
    '''
    This function should return num_1 * num_2. Replace the line below with the
    correct code.
    '''
    return num_1 * num_2


def DivideNumbers(num_1, num_2):
    '''
    This function should return num_1 / num_2. If there is a divide by 0 error,
    return the string 'Error'. Repalce the line below with the correct code.
    '''
    if (num_2 == 0):
        return 'Error'
    return num_1 / num_2


# You don't need to change anything below this line.
num_1 = float(input("Enter first number: "))
num_2 = float(input("Enter second number: "))

print(num_1, "+", num_2, "=", AddNumbers(num_1, num_2))
print(num_1, "-", num_2, "=", SubtractNumbers(num_1, num_2))
print(num_1, "*", num_2, "=", MultiplyNumbers(num_1, num_2))
print(num_1, "/", num_2, "=", DivideNumbers(num_1, num_2))
