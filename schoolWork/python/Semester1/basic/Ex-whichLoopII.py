secret_num = 123
guess = None
while guess != secret_num:
    guess = int(input("Guess num:"))
    if guess < secret_num:
                print("too low! Try again")
    else:
        print("too high! try again")
    print("you gueseed it")
