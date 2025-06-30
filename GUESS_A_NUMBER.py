import random

computer_number = random.randint(1,100 + 1)



while True:
    player_input = input("Please enter a number from 1 to 100: ")

    if not player_input.isnumeric():
        print("Not a number")
        quit()

    if int(player_input) == computer_number:
        print(f"Bingo! {computer_number}")
    elif int(player_input) < computer_number:
        print("Too low")
    elif int(player_input) > computer_number:
        print("Too High")
