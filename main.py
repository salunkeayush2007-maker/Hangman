import random
import hangman_art
import hangman_words


lives = 6

print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
wrong_guessed_letters = []
while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()


    display = ""

    if guess in correct_letters:
         print(f"You've already guessed {guess}")
         continue
    
    
    for letter in chosen_word:
            
                
                
        if letter == guess:
            display += letter
            
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    
    if guess in chosen_word:
        correct_letters.append(guess)        

    print("Word to guess: " + display)
    
    if guess in wrong_guessed_letters:
            print(f"You've already guessed {guess}")


    elif guess not in chosen_word:
        wrong_guessed_letters.append(guess)
        print(f"You guessed {guess}, that's not in the word.\n You lost a life!")
        lives-= 1
        
    
        

        if lives == 0:
            game_over = True

            print(f"***********************YOU LOSE**********************")
            print(f"The correct word was: {chosen_word}")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(hangman_art.stages[lives])