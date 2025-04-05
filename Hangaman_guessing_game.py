import random

words = ['hangaman','game','name','player','guesses','word','life','enjoyment']

def choose_word():
    return random.choice(words)

def find_guess(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += '_'
        
    return displayed_word
        
def hangaman():
    guessed_word = choose_word()
    guess_num = 9 
    guessed_letters = []
    print("No. of guesses is limited to only 9 times")

    print("Welcome to Hangman!")
    print("Try to guess the word.")

    while guess_num > 0:  
        print("\nWord: ",find_guess(guessed_word, guessed_letters))

        guess = input("Enter the letter of your choice: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please! enter a single letter... ")
            continue

        if guess in guessed_letters:
            print("You have guessed correctly!!")
            break

        guessed_letters.append(guess)

        if guess not in guessed_word:
            print("Incorrect guess!")
            guess_num = guess_num - 1
        else:
            print("Correct guess!!")

        if '_' not in find_guess(guessed_word, guessed_letters):
            print("Congrats! You guessed the word: ",guessed_word)
            break

    if guess_num == 0:
        print("\nSorry! you ran out of the attempts.\nThe word was: ",guessed_word)
        
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        hangaman()
    else:
        print("Thank you for playing!!")

hangaman()
