secret_word = "Alvaro"
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
    dashes = ""
    for i in range(len(secret_word)):
        dashes = dashes + "-"
    while (1):
        print(dashes)
        for i, dashcheck in enumerate(dashes):
            dash_count = 0
            if dashcheck=="-":
                dash_count = dash_count + 1
            else:
                continue
        if dash_count != 0:
            letter = retrieve_guess()
            for i, word in enumerate(secret_word):
                if letter == word:
                    dashes = dashes[:i] + letter + dashes[i + 1:]
                else:
                    continue
        else:
            print("You won!")
            break


update_dashes()
