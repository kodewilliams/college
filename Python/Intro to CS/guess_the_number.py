def GuessTheNumber(mystery_num):
    # Continually ask the user for guesses until they guess correctly.

    num_guesses = 0
    user_guess = 0

    while user_guess != mystery_num:
        num_guesses += 1
        user_guess = int(input('Enter a guess: '))
        if user_guess > mystery_num:
            print ('Too high!')
        elif user_guess < mystery_num:
            print ('Too low!')

    print ('You\'re correct! It took you', num_guesses, 'guesses.')


GuessTheNumber(13)
print()
GuessTheNumber(-1)
print()
GuessTheNumber(5)
