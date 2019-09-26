print("Length of guess word is atleast five and related to animal name.")

secret_words ="horse"
guess = ""
guess_count = 0
guess_limit = 9
out_of_guess = False

while guess != secret_words and not(out_of_guess):
    if guess_limit >= guess_count:
        guess = input("Enter the guess:")
        guess_count += 1
    else:
        out_of_guess = True

if out_of_guess:
    print("you lose")
else:
    print("you win")