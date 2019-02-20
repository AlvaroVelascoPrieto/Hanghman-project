secret_word = "Alvaro"
gol= False


    while True:
        if x is True:
            return guess
        else:
            global guess
            guess = input("Enter a lowercase letter: ")
            for i in guess:
                if i.islower()==False:
                    print("Your letter must be lowercase!")
                elif len(guess) != 1:
                    print("You can only enter 1 letter!")
                    break
                elif len(guess)==1 and i.islower()==True:
                    x= True
                    break
                else:
                    break




print(guess)