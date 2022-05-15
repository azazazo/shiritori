import json

with open("words_dictionary.json", "r") as read_file:
    print("Converting JSON encoded data into Python dictionary")
    dictionary = json.load(read_file)

# put any libraries needed here
# you should not use any global variables

import random


# Task 1 - Game functions
# Complete Task 1 below, read question paper for details. #########
# 1.1 #########
def inDictionary(word):
    return word in dictionary


# 1.2 #########
def processCommand(command, forbidden, wordlist):
    if command == "/help":
        return helpString()
    elif command == "/rules":
        return rulesString() + "In case you've forgotten, the forbidden letter is " + forbidden
    elif command == "/wordlist":
        return wordlist
    else:
        return "Invalid command!"


# 1.3 #########
def changePlayer(currentPlayer, noPlayers, kickedOut):
    nextPlayer = currentPlayer + 1
    while nextPlayer in kickedOut or nextPlayer > noPlayers:
        if nextPlayer > noPlayers:
            nextPlayer = 1
        else:
            nextPlayer += 1
    return nextPlayer


# 1.4 #########
def playerStats(i, score, kickedOut):
    statsString = "Player " + str(i) + ": " + str(score[i - 1])
    if i in kickedOut:
        statsString += " (OUT)"
    return statsString


# DO NOT REMOVE OR EDIT the following two functions #########
def helpString():
    return """
    To view rules again, enter: /rules
    To view used words up till now, enter: /wordlist
    To view this helpscreen again, enter: /help"""


def rulesString():
    return """Rules:
A) A sample word will be given to start you off.
B) Each player must take turns inputting a word.
C) The word input must:
  1) not end with a 'forbidden' letter which will be generated later,
  2) not have been used previously,
  3) start with the last letter of the previous word,
  4) be a legitimate English word.

D) If the input word:
---- breaks the 1st rule, you will be immediately eliminated,
---- breaks the 2nd to 4th rule, there is no penalty,
---- points are awarded corresponding to the length of the word.
E) The last player standing is the winner.
"""


# Task 2 - Game Logic
# Complete Task 2 below, read question paper for details. #########

def main():
    startGame()
    noPlayers = int(input("Enter the number of players: "))
    startingWord = "apple"
    scores = []
    kickedOut = [0]
    wordlist = []
    currentPlayer = 1
    for i in range(noPlayers):
        scores.append(0)
    forbiddenChar = chr(random.randint(97, 122))
    print("You must not create a word that ends with the letter:", forbiddenChar)
    print("Your starting word is:", startingWord)
    currentWord = startingWord
    wordlist.append(currentWord)
    while len(kickedOut) < noPlayers:
        temp = 0
        print()
        print("The current word is:", currentWord)
        currentInput = str.lower(input("Player " + str(currentPlayer) + ": "))
        k = 0
        while temp != 1:
            if k > 0:
                print("The current word is:", currentWord)
                currentInput = str.lower(input("Player " + str(currentPlayer) + ": "))
            if currentInput[0] == "/":
                print(processCommand(currentInput, forbiddenChar, wordlist), "\n")
            elif currentInput in wordlist:
                print("INVALID PLAY: You cannot use a word that has been used before. \n")
            elif not inDictionary(currentInput):
                print("INVALID PLAY: Word is not an English word. \n")
            elif currentInput[len(currentInput) - 1] == forbiddenChar:
                print("Player " + str(currentPlayer) + " is out!")
                kickedOut.append(currentPlayer)
                kickedOut.sort()
                break
            elif currentInput[0] != currentWord[len(currentWord) - 1]:
                print("INVALID PLAY: Word should start with the last letter of previous word. \n")



            else:
                print("VALID PLAY")
                wordlist.append(currentInput)
                scores[currentPlayer - 1] += len(currentInput)
                currentWord = currentInput
                temp = 1

            k += 1

        currentPlayer = changePlayer(currentPlayer, noPlayers, kickedOut)
        print("SCORES:")
        for i in range(noPlayers):
            print(playerStats(i + 1, scores, kickedOut))

    for winner in range(1, noPlayers + 1):
        if winner not in kickedOut:
            print("The game has ended. Player " + str(winner) + " wins!")
            return winner, scores[winner - 1]


# DO NOT REMOVE OR EDIT any of the code below #########
def startGame():
    print("""
 _______  __   __  ___   ______    ___   _______  _______  ______    ___  
|       ||  | |  ||   | |    _ |  |   | |       ||       ||    _ |  |   | 
|  _____||  |_|  ||   | |   | ||  |   | |_     _||   _   ||   | ||  |   | 
| |_____ |       ||   | |   |_||_ |   |   |   |  |  | |  ||   |_||_ |   | 
|_____  ||       ||   | |    __  ||   |   |   |  |  |_|  ||    __  ||   | 
 _____| ||   _   ||   | |   |  | ||   |   |   |  |       ||   |  | ||   | 
|_______||__| |__||___| |___|  |_||___|   |___|  |_______||___|  |_||___| 

Welcome to Shiritori, the traditional Japanese word game in English!

""")
    print(rulesString())
    print("Good luck and have fun! :)")
    print("------------------------------------------------------------------------")


main()
