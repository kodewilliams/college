def CountVowels(word):
    # Create counter to store number of vowels
    count = 0

    # Iterate through each letter and check if it is a vowel and add it to the vowel count if it is
    for letter in word:
        if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
            count += 1

    # Return the integer value for number of vowels
    return count


print(CountVowels('pizza'))
