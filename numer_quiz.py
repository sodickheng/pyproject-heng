import random

top_of_range = input("Type a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Please type a number higher than zero ')
        quit()
else:
    print('Please type a number next time')
    quit()

random_number = random.randint(0,top_of_range)
#print(f'random-number : {random_number}')

guesses = 0

while True:
    user_guess = input("Make a guess ")
    guesses += 1
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time')
        continue
    if user_guess == random_number:
        print("You got it")
        break
    else:
        print("You got it wrong")
        if user_guess < random_number:
            print("You gussed too low")
        else:
            print("You guess too high")

print(("You got it, you have guessed total ",guesses, " times"))
