print("Welcome to quiz game")
playing = input("  Do you want to play quiz game? ")

if playing.lower() != "yes":
    quit()
print("Okay let's play quiz game")
score = 0

# question 1
answer = input("What is CPU? ")
if answer == "central processing unit":
    print("Correct")
    score += 1
else:
    print("incorrect")

# question 2
answer = input("What is GPU? ")
if answer == "graphic processing unit":
    print("Correct")
    score += 1
else:
    print("incorrect")

# question 3
answer = input("What is RAM? ")
if answer == "random access memory":
    print("Correct")
    score += 1
else:
    print("incorrect")

print(f'Total score:{score}')
print('You have ' + str(score) + ' question correct')

