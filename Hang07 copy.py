from operator import indexOf
from pdb import Restart
from random import random
from re import T
from turtle import update

def readWordsIntoList(nameOfFile):
    allWords = []
    actualFileOpened = open( nameOfFile, "r" )

    line = actualFileOpened.readline()
    line = line.rstrip( "\n" ).strip()

    while line != "":
        allWords.append( line )
        line = actualFileOpened.readline()
        line = line.rstrip( "\n" ).strip()

    # Return all the words    
    return allWords

def printAllWords( theListOfAllWords ):
    print( theListOfAllWords )



def main():
    nameOfFile = "words.txt"
    allWordsRead = []

    allWordsRead = readWordsIntoList( nameOfFile )
    printAllWords( allWordsRead )
main()   

def gameplay(allWords):
    word = random.selection(allWords)
    # word = "tonight"
    word_progress = list('-' * len(word))
    word_check = [*word]
    
    # playing = True
    guesses = 6

    print("Let's play Hangman!!")
    print(word_progress)
    
    while guesses > 0:
        print('Choose a word or letter')
        print(f'Guesses left: {guesses}')
        guess = input('')
        lettercheck = False
        
        if len(guess) == 1:
            for index in range(len(word_check)):
                if word_check[index] == guess:
                    lettercheck = True
                    word_progress[index] = guess
            print(word_progress)
            if lettercheck == False:
                print('Sorry ' + guess + ' is not present in the word')
                guesses-=1
        else:
        
            if guess == word:
                print(word_check)
                print("You Win!!")
                break
            elif guess.strip() != "":
                print("Sorry that guess is incorrect")
                guesses -=1
        if word_check == word_progress:
            print("You Win!! ")
            break
 
    
    if guesses == 0:
        print('Sorry you are a deadman GAMEOVER')
    # else:
    #     print('gameover')

    replay = input("Would you like to play a game? Y/N ")
    if replay == "Y" or replay == "y":
        gameplay()
    else:
        print("Enjoy your day")






#     #defining user loss conditions
#     if guesses == 0:
#         print('Sorry you are dead would you like to try again?')
gameplay()