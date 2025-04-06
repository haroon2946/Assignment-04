import random

print("\n ✨Welcome to the Number Guessing Game.✨ \n")
print("\n 💻 Computer will try to guess your number. \n")

low = 1
high = 10

print("🤔 Think of a number between 1 and 10, and 💻 will try to guess it!")

while low <= high:
    guess = random.randint(low, high)
    print(f"\n🤖 Is your number {guess}?")
    
    feedback = input(" 👉 Enter 'h' for too high, 'l' for too low, or 'c' if correct: ").lower()

    if feedback == 'h':
        high = guess - 1
    elif feedback == 'l':
        low = guess + 1
    elif feedback == 'c':
        print(f"\n🎉 Yay! 💻 guessed the number {guess} correctly. 🎉")
        break
    else:
        print("⚠️ Invalid input. Please enter only 'h', 'l', or 'c'. 🚫")

if low > high:
    print("\n😅 Hmm... It seems there was a misunderstanding or incorrect feedback. Let's try again! 🔄")
