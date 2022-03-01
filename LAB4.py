# *****************************************************************************************************************************************************************************************
# Author: Najeb Johnson
# Lab: Lab 4
# Date: 2/27/2022
# Description   Example: This program is a simple rock paper scissors game
# Input: rock, paper, or scissors
# Output: rock beats scissors, scissors beat paper, paper beats rock
# Sources: https://www.youtube.com/watch?v=eF5mObNHeek,
# https://www.youtube.com/watch?v=KzqSDvzOFNA,
# https://www.youtube.com/results?search_query=python+random+while
# Terrell K a fellow student helped me out
# ****************************************************************************************************************************************************************************************

import random


# Get computers choice
def get_computer_choice():
    return random.choice(["scissors", "paper", "rock"])


# Get users choice and take value of choice as a default parameter
def get_user_choice(choice):
    prompt = "Enter scissor, paper or rock\n"
    choice = input("%s" % prompt)
    try:
        ["rock","scissor","paper"].index(choice)
    except ValueError:
        print(prompt)
        choice = ''
        get_user_choice(choice)

    return choice


def main():
    user_choice = ''
    while user_choice != 'q':
        computer_choice = get_computer_choice()
        user_choice = get_user_choice(user_choice)
        winner = calculate_winner(user_choice, computer_choice)
        print(winner)


def calculate_winner(choice, computer_choice):
    if choice == computer_choice:
        return f"The Computer chose {computer_choice}, so there seems to be a tie"
    elif choice == "rock" and computer_choice == "scissors" or choice == "rock" and computer_choice == "paper" \
            or choice == "paper" and computer_choice == "rock":
        return f"The Computer chose {computer_choice} and you chose {choice}. You Win!"
    else:
        return f"The Computer chose {computer_choice} and you chose {choice}. You lose!"


main()

