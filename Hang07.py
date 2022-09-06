import random

#copies words into list to be randomly selected from later
def readWordsIntoList(wordFileName):
    allWords = []
    actualFileOpened = open( wordFileName, "r" )

    line = actualFileOpened.readline()
    line = line.rstrip( "\n" ).strip()

    while line != "":
        allWords.append( line )
        line = actualFileOpened.readline()
        line = line.rstrip( "\n" ).strip()
    actualFileOpened.close()

    # Return all the words    
    return allWords

# Checks if allWords took words from txt file
def printAllWords( theListOfAllWords ):
    print( theListOfAllWords )


# selects file to copy words from
def main():
    nameOfFile = "words.txt"
    allWords = []

    allWords = readWordsIntoList( nameOfFile )
    #runs word check function
    # printAllWords( allWords )
    gameplay( allWords, nameOfFile )

def addWords(wordFileName):
    addWords = input("Would you like to add words to our little game? Y/N ")
    if addWords == "Y" or addWords == "y":
        wordAdded = input ("Spell out a word to save to the game: ")
        file = open( wordFileName, "a" )
        file.write('\n' + wordAdded )
        file.close()
        print( wordAdded + ' added.')
    
    
   
#the actual gqameplay
def gameplay(allWords, wordFileName):
    word = random.choice(allWords)
    # word = "tonight"
    word_progress = list('-' * len(word))
    word_check = [*word]
    guesses = 6
    winner = False

    

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
                print("You Win!!")
                winner = True
                break
            elif guess.strip() != "":
                print("Sorry that guess is incorrect")
                guesses -=1
        if word_check == word_progress:
            print("You Win!! ")
            winner = True
            break
 
    
    if guesses == 0:
        print('Sorry you are a deadman GAMEOVER')
        print(word)
    
    if winner == True:
        addWords(wordFileName)
    
    replay = input("Would you like to play another game? Y/N ")
    if replay == "Y" or replay == "y":
        gameplay(allWords, wordFileName)
    else:
        print("Enjoy your day")

main()




#     #defining user loss conditions
#     if guesses == 0:
#         print('Sorry you are dead would you like to try again?')
