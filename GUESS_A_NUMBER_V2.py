def player_input_check(inp :str)->bool:
    return inp.isnumeric()

def new_game(action :str):
    if action.lower() == "y":
        return main_game()
    elif action.lower() == "n":
        return "Exiting game"
    else:
        "invalid input"

def main_game():

    import random

    computer_number = random.randint(1,100 + 1)

    initial_tries = 5
    num_tries = initial_tries

    while num_tries > 0:
        player_input = input("Please enter a number from 1 to 100: ")

        if not player_input_check(player_input):
            return "Invalid number"

        if int(player_input) == computer_number:
           return f"Bingo! You found number {computer_number}\nYou won with {initial_tries - num_tries} tries!"

        elif int(player_input) < computer_number:
            num_tries -= 1
            print("Too low")
        elif int(player_input) > computer_number:
            num_tries -= 1
            print("Too High")

    else:
        return "You lose"

if main_game() == "You lose" or "Invalid number":
    player_action = input("Would you like to try again Y/N?")
    print(new_game(player_action))

