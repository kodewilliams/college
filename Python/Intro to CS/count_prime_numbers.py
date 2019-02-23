def IsPrime(n):
    # Set to lowest prime number and start there
    i = 2
    # Set variable to flag composite number if found
    prime = True
    
    while i <= n // 2:
        if n % i == 0:
            prime = False
        i = i + 1
        
    return prime


def CountPrimeNumbers(nums):

    count = 0

    for num in nums:
        if num > 1:
            if num == 2:
                count = count + 1
                continue

            if IsPrime(num):
                count = count + 1
                
    return count


print(CountPrimeNumbers([4, 7, 8, 11, 17]))
print(CountPrimeNumbers([27281, 23547, 23549, 23551, 41661]))
print(CountPrimeNumbers([-3, -2, -1, 0, 1, 2, 3]))
print(CountPrimeNumbers([]))
