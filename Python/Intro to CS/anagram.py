def stripAndSort(word):
    for letter in word:
        if letter == ' ':
            word.remove(letter)
            
    for i in range(len(word)):
        for j in range(len(word)-i-1):
            if word[j] > word[j+1]:
                temp = word[j]
                word[j] = word[j+1]
                word[j+1] = temp
    return word
    

def IsAnagram(word1, word2):
    # Convert words to lists, strip both lists of spaces and sort them.
    word1 = stripAndSort(list(word1))
    word2 = stripAndSort(list(word2))
    
    # If strings aren't the same length, not anagrams.
    if len(word1) != len(word2):
        return False
    else:
        # Compare both strings.
        if word1 != word2:
            return False
        return True



# Program checking if you so desire.
# Yes, I know that is an infinite loop, sorry.

while True:
    # Ask user for two strings.
    word1 = input('First word: ')
    word2 = input('Second word: ')

    # Return value
    print(IsAnagram(word1, word2))
    print()
