import random

    #randomly select a number
rand_num = random.randint(0,100)

def start_game():
    print(
        "Welcome to the number guessing game!\n"
        "I'm thinking of a number between 1 and 100.\n"
        "Please select the difficulty level:\n"
        "1. Easy (10 Chances)\n"
        "2. Medium (5 Chances)\n"
        "3. Hard (3 Chances)\n"
    )
    difficulty = int(input("Enter your choice: "))
    if difficulty == 1:
        play_game(10)
    elif difficulty == 2:
        play_game(5)
    elif difficulty == 3:
        play_game(3)
    else:
        print("Please choose a valid difficulty (1, 2, or 3)")

def play_game(attempts):
    while True:
        choice = int(input("Enter your guess: "))

        attempts -= 1

        if choice == rand_num:
            print(f"Congratulations! You guessed the correct number with {attempts} attempts remaining!")
            break
        elif attempts == 0:
            print("Sorry you were unable to guess the number!")
            break
        elif choice < rand_num:
            print(f"Incorrect! The number is greater than {choice}.")
        else:
            print(f"Incorrect! The number is smaller than {choice}.")
    play_again()

def play_again():
    replay = input("Do you want to play again?(Y/N)").upper()
    if replay == "Y":
        start_game()
    elif replay == "N":
        print("Have a good day!")
    else:
        print("Please select Y/N")
        play_again()


def main():

    start_game()

if __name__ == "__main__":
    main()