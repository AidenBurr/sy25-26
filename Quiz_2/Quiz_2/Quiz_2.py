# set number equal to your number 
# get the persons input for the number theyre guessing

number = 3
max_attempts = 5
attempt = 0

while attempt < max_attempts:
    attempt += 1
    guess = int(input(f"Attempt {attempt}: Guess a number between 1 and 10: "))
    if guess == number:
        print("You got it!")
        break
    else:
        print("Wrong! Try again.")
else:
    print(f"Sorry, you've used all {max_attempts} attempts. The number was {number}.")