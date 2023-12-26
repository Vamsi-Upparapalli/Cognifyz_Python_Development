import random

def computer_guess(low, high):
    guess = random.randint(low, high)
    return guess

def computer_guessing_game():
    print("Welcome to the number guessing game!")
    print("I will guess a number between 1 and 100.")

    low = 1
    high = 100
    while True:
        try:
            answer = input("Am I right? Enter 'h' if my guess is too high, 'l' if my guess is too low, or 'c' if my guess is correct: ")
        except ValueError:
            print("Sorry, your answer must be 'h', 'l', or 'c'.")
            continue

        guess = computer_guess(low, high)
        print("I guessed the number", guess)

        if answer.lower() == 'h':
            if guess < high:
                low = guess + 1
            else:
                print("I can't guess any higher without going over 100.")
        elif answer.lower() == 'l':
            if guess > low:
                high = guess - 1
            else:
                print("I can't guess any lower without going under 1.")
        elif answer.lower() == 'c':
            print("Great job! I guessed your number correctly!")
            break
        else:
            print("Sorry, your answer must be 'h', 'l', or 'c'.")

if __name__ == "__main__":
    computer_guessing_game()