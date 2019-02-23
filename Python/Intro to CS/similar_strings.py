def AreStringsSimilar(str1, str2):
    # If string lengths differ by more than one, not similar.
    if abs(len(str1)-len(str2)) > 1:
        return False
    else:
        # Break up words into their own dictionaries.
        word1 = list(str1)
        word2 = list(str2)

        # Keep a status of the number of differences between two strings.
        differences1 = 0
        differences2 = 0

        # Check to see if the other word contains one difference or less.
        for key in word1:
            if not(key in word2):
                differences1 += 1

        for key in word2:
            if not(key in word1):
                differences2 += 1

        # If it contains more than one, return False. Else, true.
        if differences1 <= 1 and differences2 <= 1:
            return True
        else:
            return False

        
# Ask user for two strings.
str1 = input('First string: ')
str2 = input('Second string: ')

# Return True or False if strings are similar or not.
print(AreStringsSimilar(str1, str2))
