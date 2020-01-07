# -*- coding: utf-8 -*-
import random

IMAGES=['''
    +---+
    |   |
        |
        |
        |
        |
        =========''','''
    +---+
    |   |
    0   |
        |
        |
        |
        =========''','''
    +---+
    |   |
    0   |
    |   |
        |
        |
        =========''','''
    +---+
    |   |
    0   |
   /|   |
        |
        |
        =========''','''
    +---+
    |   |
    0   |
   /|\  |
        |
        |
        =========''','''
    +---+
    |   |
    0   |
   /|\  |
    |   |
        |
        =========''','''
    +---+
    |   |
    0   |
   /|\  |
    |   |
   /    |
        =========''','''
    +---+
    |   |
    0   |
   /|\  |
    |   |
   / \  |
        =========''','''
   ''']     

WORDS=[
    'washer ',
    'drier',
    'couch',
    'pencil',
    'dog',
    'computer',
    'keyboard',
    'car',
    'mouse',
    'steam',
    'fin '
    'shair'
]
def displayBoard(hidden_word,tries,num):
    print(IMAGES[tries])
    print("")
    print(hidden_word)
    print(("*----"*num) +"*")

def randomWord():
    id_ran=random.randint(0,len(WORDS)-1)
    return WORDS[id_ran]

def run():
    word=randomWord()
    hidden_word=["-"]*len(word)
    tries=0

    while True:
        displayBoard(hidden_word,tries,len(word))
        trie_letter=str(raw_input("Enter a letter: "))

        letter_indexes=[]
        for i in range(len(word)):
            if word[i]==trie_letter:
                letter_indexes.append(i)

        if len(letter_indexes)==0:
            tries+=1

            if tries==len(IMAGES)-2:
                displayBoard(hidden_word,tries,len(word))
                print("")
                print("Y O U   L O S E  :(")
                print("The correct word is: "+word)
                break
            
        else:
            for i in letter_indexes:
                hidden_word[i]=trie_letter
                
            letter_indexes=[]

        try:
            hidden_word.index("-")
        except ValueError:
            print("|-----------------------|")
            print(" !! Y O U    W I N !! :3")
            break
    



if __name__ == "__main__":
    print("W E L C O M E   T O   H A N G M A N")
    run()
