
#WELCOME TO THE HANGMAN.....
import random

words=["apple","dog","cat","fish","elephant"]
secret_word=random.choice(words)

display=["_"]*len(secret_word)
count=0
max_attempts=6
guessed_words=[]

#for progress 
while count<max_attempts and "_" in display:
    print("\n Word: "," ".join(display))
    print("guessed word: ",guessed_words)
    print("attempts left: ",max_attempts-count)

    guess=input("Enter the letter: ").lower()

    if guess in guessed_words:
        print("Already used letter.")
        continue

    guessed_words.append(guess)

    if guess in secret_word:
        print("correct guess")
        for i in range(len(secret_word)):
            if secret_word[i]==guess:
                display[i]=guess

    else:
        print("Guess is wrong")
        count+=1

if "_" not in display:
    print("\nCongratulations you won,the word was: ",secret_word)

else:
    print("Fail you guessed wrong")

