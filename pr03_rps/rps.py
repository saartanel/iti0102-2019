"""Simple version of rock paper and scissors."""
from random import choice


def normalize_user_name(name: str) -> str:
    """
    Simple function gets player name as input and capitalizes it.

    :param name: name of the player
    :return: A name that is capitalized.
    """
    name = name.title()
    return name


def reverse_user_name(name: str) -> str:
    """
    Function that takes in name as a parameter and reverses its letters. The name should also be capitalized.

    :param name: name of the player
    :return: A name that is reversed.
    """
    name = name[::-1].title()
    return name


def check_user_choice(choice: str) -> str:
    """
    Function that checks user's choice.

    The choice can be uppercase or lowercase string, but the choice must be
    either rock, paper or scissors. If it is, then return a choice that is lowercase.
    Otherwise return 'Sorry, you entered unknown command.'
    :param choice: user choice
    :return: choice or an error message
    """
    if any(i in choice.lower() for i in (["rock", "paper", "scissors"])):
        choice = choice.lower()
        return choice
    else:
        return "Sorry, you entered unknown command."
    pass


def determine_winner(name: str, user_choice: str, computer_choice: str, reverse_name: bool = False) -> str:
    """
    Determine the winner returns a string that has information about who won.

    You should use the functions that you wrote before. You should use check_user_choice function
    to validate the user choice and use normalize_user_name for representing a correct name. If the
    function parameter reverse is true, then you should also reverse the player name.
    NB! Use the previous functions that you have written!

    :param name:player name
    :param user_choice:
    :param computer_choice:
    :param reverse_name:
    :return:
    """
    winner = ""
    if reverse_name:
        name = name[::-1].title()
    name = name.title()
    if any(i in user_choice.lower() for i in ["rock", "paper", "scissors"]) and \
            any(i in computer_choice.lower() for i in ["rock", "paper", "scissors"]):
        user_choice = user_choice.lower()
        computer_choice = computer_choice.lower()
        if user_choice == computer_choice:
            return name + " had " + user_choice + " and computer had " + computer_choice + ", hence it is a draw."
        elif user_choice == "rock" and computer_choice == "scissors":
            winner = name
        elif user_choice == "scissors" and computer_choice == "paper":
            winner = name
        elif user_choice == "paper" and computer_choice == "rock":
            winner = name
        elif user_choice == "paper" and computer_choice == "scissors":
            winner = "computer"
        elif user_choice == "scissors" and computer_choice == "rock":
            winner = "computer"
        elif user_choice == "rock" and computer_choice == "paper":
            winner = "computer"
    else:
        return "There is a problem determining the winner."
    return name + " had " + user_choice + " and computer had " + computer_choice + ", hence " + winner + " wins."


def play_game() -> None:
    """
    Enable you to play the game you just created.

    :return:
    """
    user_name = input("What is your name? ")
    play_more = True
    while play_more:
        computer_choice = choice(['rock', 'paper', 'scissors'])
        user_choice = check_user_choice(input("What is your choice? "))
        print(determine_winner(user_name, user_choice, computer_choice))
        play_more = True if input("Do you want to play more ? [Y/N] ").lower() == 'y' else False


if __name__ == "__main__":
    print(normalize_user_name('ago'))  # Ago
    print(normalize_user_name('AGO'))  # Ago
    print(normalize_user_name('MaRtInA'))  # Martina

    print(reverse_user_name('MaRtInA'))  # Anitram
    print(reverse_user_name('AGO'))  # Oga

    print(check_user_choice('rock'))  # rock
    print(check_user_choice('ROCK'))  # rock
    print(check_user_choice('midagi on viltu'))  # Sorry, you entered unknown command.

    # 50% on juba tehtud, tubli töö!

    print(determine_winner('ago', 'rock', 'rock'))  # Ago had rock and computer had paper, hence computer wins.
    print(determine_winner('aGO', 'rock', 'paper', True))  # Oga had rock and computer had paper, hence computer wins.
    print(
        determine_winner('loORa', 'SCISSORS', 'paper'))  # Loora had scissors and computer had paper, hence Loora wins.
    print(determine_winner('Shakira', 'waka waka', 'fire'))  # There is a problem determining the winner.
    print(determine_winner('Shakira', 'rock',
                           'sciSSOrs'))  # Shakira had rock and computer had scissors, hence Shakira wins.

    play_game()  # Kommenteeri see rida välja kui kõik funktsioonid on valmis
