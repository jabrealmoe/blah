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

# Function user_input():
# display("Rock Paper Scissor Game")
# Declare global variable possible_choice equal to ["rock", "paper", "scissor", ]
# Set x equal to input("Enter rock, paper, scissor")
# while x not in possible_choice:
# Display ('please enter rock, paper, or scissor')
# X is equal to re enter input("Enter rock, paper, scissor")
# End while statement
# computer_choice equal to random.choice(possible_choice)
# Display (computer chose {computer_choice} ')
# if x equal to computer_choice:
# Display("it's a tie")
# Else if  x is equal to "paper":
# Call function   paper(x, computer_choice)
# Else if  x is equal to "scissors":
# Call function  scissors(x, computer_choice)
# Else if x is equal to "rock":
# Call  if  rock(x, computer_choice)
# End Function


def user_input():
    print("Beat The Computer at a rock paper scissors game!")
    possible_choices = ["rock", "paper", "scissor", ]
    rock_paper_scissors = "Enter rock, paper or scissor:\n"
    choice = input(rock_paper_scissors)
    while choice not in possible_choices:
        print(rock_paper_scissors)
        choice = input(rock_paper_scissors)
    computer_choice = random.choice(possible_choices)
    if choice == computer_choice:
        print(f"computer chose {computer_choice} it's a tie")
    elif choice == "paper":
        paper(choice, computer_choice)
    elif choice == "scissors":
        scissors(choice, computer_choice)
    elif choice == "rock":
        rock(choice, computer_choice)

# Function rock(x,computer_choice):
# if x equal to "rock":
# if computer_choice equal to "paper":
# Display('''paper beats you lose!''')
# End If statement
# Or else:
# Display ('''rock beats sciss you win!''')
# End If statement
# End Function


def rock(x, computer_choice):
    if x == "rock":
        if computer_choice == "paper":
            print('''paper beats rock! you lose!''')
        else:
            print('''rock beats scissors you win!''')

# Function paper(x,computer_choice):
# if x equal to "paper":
# if computer_choice equal to"scissors":
# Display('''scissors beat paper you lose!''')
# Or else:
# Display ('''paper beats rock! you win!''')
# End If statement
# End Function


def paper(x,computer_choice):
    if computer_choice == "scissors":
        print('''scissors beat paper! you lose!''')
    else:
        print('''paper beats rock! you win!''')
# Function scissors(x, computer_choice):
# if x equal to "scissors":
# if computer_choice equal to "rock":
# Display ('''rock beats scissors! you lose!''')
# End If statement
# Or else else:
# Display('''scissors beat paper! you win!''')
# End If statement
# End Function

def scissors(x, computer_choice):
    if x == "scissors":
        if computer_choice == "rock":
            print('''rock beats scissors!
                you lose!''')
        else:
            print('''scissors beat paper!
                you win!''')

# Module main():
#   play is equal to True
#   while play is true:
#       Call user_input()
#       Play = "Placeholder"
#       While play is not yes or no
#       try:
#           play is equal to "y": True, "n": False / user input "Do you want to play again? y/n"
#           Except for a KeyError:
#               Display("please enter y or n")
# End Module

# Call module main()

def main():
    play = True
    while play:
        user_input()
        play = "Placeholder"
        while play not in (True, False):
            try:
                play = {"y": True, "n": False}[input("Do you want to play again? y/n  ").lower()]
            except KeyError:
                print("please enter y or n")


main()
