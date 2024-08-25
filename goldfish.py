#!/usr/bin/env python3
# This script allows you to play gold fish

# Imports
import os
import random


os.system('clear')
print("Gold fish where the object is to win!!\n\n\n\n\n")

deck = ["2H","3H","4H","5H","6H","7H","8H","9H","10H","JH","QH","KH","AH",
        "2S","3S","4S","5S","6S","7S","8S","9S","10S","JS","QS","KS","AS",
        "2C","3C","4C","5C","6C","7C","8C","9C","10C","JC","QC","KC","AC",
        "2D","3D","4D","5D","6D","7D","8D","9D","10D","JD","QD","KD","AD"]

# Shuffle the deck
num_shuffle = int(input("How many times do you want to shuffle the deck: "))
print("Shuffling the deck" ,num_shuffle, "times\n")
for i in range (num_shuffle) :
    random.shuffle(deck)

print("Shuffled Deck \n" , deck, "\n\n\n\n\n")

player_hand = 7

player_1 = []
player_2 = []
for i in range (player_hand) :
    player_1.append(deck.pop(0))
    player_2.append(deck.pop(0))



print(len(player_1))
print("Player 1 ", player_1, "\n\n\n\n\n")
print(len(player_2))
print("Player 2 ", player_2, "\n\n\n\n\n")
print(len(deck))
print("Deck ", deck, "\n\n\n\n")
