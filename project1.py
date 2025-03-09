import random


categories = {
    "Sports": ["basketball", "badminton", "archery", "volleyball", "football", "cricket"],
    "Movies": ["Action", "Thriller", "Comedy", "Drama", "Romance", "Sci-fi"],
    "Animal": ["Rhinoceros", "Octopus", "Kangaroo", "Elephant", "Penguin", "Koala"],
    "Apps": ["Whatsapp", "Facebook", "Instagram", "Snapchat", "Pinterest", "Zepto"],
    "Colour": ["Magenta", "Lilac", "Turquoise", "Lavender", "Fuchsia", "Orchid"],
}


name = input("Enter your name: ")

print("\nWelcome to the Guessing Game,",name,"!")
print("You have 10 chances to guess the correct word.")
print("Let's Start!!\n")


print("Categories:")
for category in categories.keys():
    print("-", category)


category = input("\nSelect a category: ").title()
if category not in categories:
    print("Invalid category! Restart the game and choose a valid category.")
    exit()


word = random.choice(categories[category]).lower()
guessed = ["_"] * len(word) 
wrong_guesses = []
chances = 10


print("\nYour word:")
print(" ".join(guessed))


while chances > 0:
    guess = input("\nEnter a character: ").lower()

    if len(guess) != 1:
        print("Please enter a valid single letter.")
        continue


    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
        print("\nCorrect guess!")
    else:
        wrong_guesses.append(guess)
        chances -= 1
        print("\nWrong guess! Chances left:", chances)

    
    print(" ".join(guessed))

    
    if "_" not in guessed:
        print("\nCongratulations,", name,"! You guessed the word:", word)
        break


if "_" in guessed:
    print("\nYou lost! The correct word was:", word)
    print("Better luck next time!")

print("\n--- Thanks for playing! ---")
