import random

# Word list for the game
word_list = ["python", "developer", "hangman", "programming", "computer"]

def get_word():
    """Selects a random word from the word_list."""
    return random.choice(word_list).lower()

def display_word(word, guessed_letters):
    """Displays the word with correctly guessed letters and underscores for missing ones."""
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def play_hangman():
    """Main function to play Hangman."""
    word = get_word()  # Select a random word
    guessed_letters = set()
    attempts = 6  # Maximum number of wrong guesses

    print("🎩 Welcome to Hangman! Try to guess the word. 🔤")
    
    while attempts > 0:
        print("\nWord:", display_word(word, guessed_letters))
        print(f"Remaining attempts: {attempts}")
        
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Invalid input! Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("⚠ You already guessed that letter!")
            continue

        guessed_letters.add(guess)
        
        if guess in word:
            print("✅ Good guess!")
            if all(letter in guessed_letters for letter in word):
                print("\n🎉 Congratulations! You guessed the word:", word)
                break
        else:
            print("❌ Wrong guess!")
            attempts -= 1
    
    if attempts == 0:
        print("\n💀 Game Over! The word was:", word)

# Running the game
if __name__ == "__main__":
    play_hangman()