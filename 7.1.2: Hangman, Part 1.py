secret_word = "Alvaro"

def retrieve_guess():
    while (1):
        guess = input("Enter a letter:")
        guess.lower()
        if len(guess) == 1:
            return guess
        else:
            print("Only 1 letter!")
            continue

