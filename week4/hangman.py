'''
The hangman game is a word guessing game where the player is given a word and has to guess the letters that make up the
word. 
The player is given a certain number of tries (no more than 6 wrong guesses are allowed) to guess the correct letters 
before the game is over.
'''

# Output
'''
You have 6 tries left.                                                                                                                                           
Used letters:                                                                                                                                                    
Word: _ _ _ _                                                                                                                                                    
Guess a letter: a 

You have 6 tries left.                                                                                                                                           
Used letters: a                                                                                                                                                  
Word: _ a _ a                                                                                                                                                    
Guess a letter: j    

You have 6 tries left.                                                                                                                                           
Used letters: j a                                                                                                                                                
Word: j a _ a                                                                                                                                                    
Guess a letter: v                                                                                                                                                
You guessed the word java !
'''


import random


def display_word(word, guessed_letters):
    result = ""
    for letter in word:
        if letter in guessed_letters:
            result += letter + " "
        else:
            result += "_ "
    return result

def random_word():
    word_list = [ "java", "python", "kreativstorn"]
    return random.choice(word_list)

def hangman():
    max_attempts = 6
    word_to_guess = random_word()
    guessed_letters = []
    attempts = 0

    print("Welcome to Hangman!")
    print("Try to guess the word within 6 attempts.")

    while attempts < max_attempts:
        print(f"\n You have {max_attempts - attempts} tries left.")
        print("Used letters:", " ".join(guessed_letters))
        print("Word:", display_word(word_to_guess, guessed_letters))

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("Good guess!")
            if all(letter in guessed_letters for letter in word_to_guess):
                print(" You guessed the word:", word_to_guess)
                break
        else:
            print("Incorrect guess.")
            attempts += 1

    if attempts == max_attempts:
        print("\n Out of tries. The word was:", word_to_guess)

if __name__ == "__main__":
    hangman()







