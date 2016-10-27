my_number = 37
print("Enter your guess: ")
guess = int(input())

if guess > my_number:
    print("Guess was too high")
elif guess < my_number:
    print("Guess was too log")
else:
    print("You got it!")