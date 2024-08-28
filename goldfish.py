#!/usr/bin/env python3
# This script allows you to play gold fish

# Imports
import os
import random
import re


os.system('clear')
print("Gold fish where the object is to win!!\n\n\n\n\n")

# This array is the deck.  Hearts, Spades, Clubs, and Diamonds
deck = ["2H","3H","4H","5H","6H","7H","8H","9H","XH","JH","QH","KH","AH",
        "2S","3S","4S","5S","6S","7S","8S","9S","XS","JS","QS","KS","AS",
        "2C","3C","4C","5C","6C","7C","8C","9C","XC","JC","QC","KC","AC",
        "2D","3D","4D","5D","6D","7D","8D","9D","XD","JD","QD","KD","AD"]




# Shuffle the deck
num_shuffle = int(input("How many times do you want to shuffle the deck: "))
print("Shuffling the deck" ,num_shuffle, "times\n")
for i in range (num_shuffle):
    random.shuffle(deck)

print("Shuffled Deck \n" , deck, "\n\n\n\n\n")

# This is the player hand size, there might be a better way to do this.
player_hand = 7

player_1 = []
player_2 = []
gofish = 0

# This is to draw each players hands.  I need to see what pop does.
for i in range (player_hand):
    player_1.append(deck.pop(0))
    player_2.append(deck.pop(0))

# How do I display player_1 hand and select a card?
print("Cards in your hand are: ", player_1, "\n")
print("Cards in player 2 hand are: ", player_2, "\n")
card_select = input("Which card would you like to pick? ")
if card_select in player_1:
    print("Card is in your hand")
    # This regex catches the first character
    pattern = r'^.'
    match = re.search(pattern, card_select)
    first_char = match.group()
    print("First character is: ", first_char)
    # This regex and enumeration use the first_char and finds the index of the matches in player_2's hand
    pattern = first_char
    for index, text in enumerate(player_2):
        match = re.search(pattern, text)
        if match:
            player_1.append(player_2.pop(index))
        else:
            gofish = 1
    if (gofish == 1):
        print("Go Fish!!!")
        player_1.append(deck.pop(0))
    # This tells us where the selected card is in the players hand
    selected_card_player_1 = (player_1.index(card_select))
else:
    print("You do not have that card in your hand")

# Strip the suit out of it.
#pattern = r'^.'
#match = re.search(pattern, card_select)
#first_char = match.group()
#print("First character is: ", first_char)
#print("Card location is ",selected_card_player_1, "\n\n\n\n\n")

# Check first digit and find in player_2 hand

# Debug print statements below

print(len(player_1))
print("Player 1 ", player_1, "\n\n\n\n\n")
print(len(player_2))
print("Player 2 ", player_2, "\n\n\n\n\n")
print(len(deck))
print("Deck ", deck, "\n\n\n\n")
