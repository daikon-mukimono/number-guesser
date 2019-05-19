import random

max_guesses = 7
guesses_left = 7

def new_game(range_top=100):
    
    global secret_number
    global guesses_left
#    global max_guesses
    global last_range
    global guesses_left

    max_guesses = 7 if range_top == 100 else 10 if range_top == 1000 else 0      #noice  

    last_range = range_top          #to use when starting a new game
    secret_number = random.randrange(range_top)
    guesses_left = max_guesses

    print("Welcome to number guesser.\n Can you guess what number I am thinking about?\n")
    input_guess(input("Enter your guess!\n"), range_top)


def range100():
    new_game()

def range1000():
    new_game(1000)

def input_guess(guess, range_top):
    int_guess = int(guess)
    global guesses_left

    if max_guesses == 0:
        print("Unexpected range input!")

    if guess < 0 or guess > range_top:
        print("Invalid input!")
        guess = input("Please enter a number within the range!\n")
    else:
        while guesses_left > 0:
            print("You guessed " + str(guess))
            guesses_left -= 1
            #compare guess to value
            if secret_number > int_guess: 
                string = "Go higher!\n"
            elif secret_number < int_guess:
                string = "Go lower!\n"
            else:
                print("Correct guess!")
                print("You win with " + str(guesses_left) + " guesses left\n")
                new_game(last_range)

            if guesses_left != 0:
                print ("You can guess " + str(guesses_left) + " more times!\n")
                input_guess(input(string), last_range)
            elif guesses_left == 0:
                print ("You're out of guesses!")
                new_game(last_range)    

new_game(input("Enter the top of the range for your game! It can be 100 or 1000\n"))