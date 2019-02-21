import random

secret_words = ["apple", "banana", "car", "computer", "programming", "science",\
                "laboratory", "printer", "box"]
secret_word = random.choice(secret_words)
secret_word = secret_word.lower()
def retrieve_guess():
    while (1):
        guess = input("Enter a letter:")
        guess.lower()
        if len(guess) == 1:
            return guess
        else:
            print("Only 1 letter!")
            continue

def update_dashes():
    try:
        dashes = ""
        guesses_left = 10
        for i in range(len(secret_word)):
            dashes = dashes + "-"
        while guesses_left != 0:
            misses_on_one_trial = 0
            print(dashes)
            print("You have " + str(guesses_left) + " incorrect guesses left")
            for i, dashcheck in enumerate(dashes):
                dash_count = 0
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
