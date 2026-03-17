import random

words=['cricket','football','hockey','badminton','squash']

word=random.choice(words)

guessed=['_']*len(word)

wrong_guesses=0


while wrong_guesses < 6 and '_' in guessed:
    print("word: "," ".join(guessed))

    letter=input("enter your letter: ").lower()
    if letter in word:
        for i in range (len(word)):
            if word[i]==letter:
               guessed[i]=letter

    else:
        wrong_guesses+=1
        print("wrong guess !")
        print("reamining guesses",6-wrong_guesses)

if "_" not in guessed:
    print("🎉 You win! Word was:", word)
else:
    print("❌ You lose! Word was:", word)
