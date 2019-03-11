#import the random labrary to use later
import random

#these are the secret words that will be used to guess in our game
secret_words = ["apple", "banana", "car", "computer", "programming", "science",\
                "laboratory", "printer", "box"]
#this two methods pick a random word and set it to be lowercase to avoid case sensitivity
secret_word = random.choice(secret_words)
secret_word = secret_word.lower()

#this function gets the user's guess
def retrieve_guess():
    while (1):
        guess = input("Enter a letter:")      #Asks the user for input
        guess.lower()                     #Sets the input to lowercase to avoid case sensitivity
        if len(guess) == 1:             #If the user input is 1 character it returns the guess
            return guess
        else:
            print("Only 1 letter!")      #if it is more than one character it loops and asks the user for input again
            continue

def update_dashes():                 #This function is the main program body
    secret_word = random.choice(secret_words)
    try:
        dashes = ""
        guesses_left = 10                       #set the number of user guesses
        for i in range(len(secret_word)):           #creates the dashes variable according to the secret word
            dashes = dashes + "-"
        while guesses_left != 0:                #while the user still has guesses left...
            misses_on_one_trial = 0
            print(dashes)                           #prints the dashes
            print("You have " + str(guesses_left) + " incorrect guesses left")     #prints the number of guesses the user has left
            dash_count = 0
            for i, dashcheck in enumerate(dashes):
                if dashcheck == "-":
                    dash_count = dash_count + 1
                else:
                    continue
            if dash_count != 0:
                letter = retrieve_guess()
                for i, word in enumerate(secret_word):
                    if letter == word:
                        dashes = dashes[:i] + letter + dashes[i + 1:]
                    else:
                        misses_on_one_trial = misses_on_one_trial + 1
                        continue
                if misses_on_one_trial == (len(secret_word)):
                    guesses_left = guesses_left - 1
            else:
                print("You won!")

                break
    except KeyboardInterrupt:
        print("Ending...")


while True:
    update_dashes()
    restart = input("Do you want to play again?(Yes/No)")
    restart.lower()
    if restart == "yes":
        continue
    if restart == "no":
        break
    else:
        print("Input not recognized!! Closing...")
        break