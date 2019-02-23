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


def PrintPrimeFactors(num):
    # Create empty list of prime factors
    primes = []

    # Loop through numbers up to half of the number and check if each number is prime
    for n in range(2, num + 1):
        if IsPrime(n):
            # If number is prime then check to see if it evenly divides and if it does,
            # it is a prime number.
            while num % n == 0 and num != 1:
                primes.append(n)
                num = num / n
        if (num == 1):
            break
        
    print (primes)


PrintPrimeFactors(24)
PrintPrimeFactors(11)
PrintPrimeFactors(1650)
PrintPrimeFactors(40378)


    
