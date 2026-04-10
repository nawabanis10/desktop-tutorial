import random

easy_words=["banana","car","ball","money","pakistan"]
medium_words=["python","computer","java","mobile","football"]
hard_words=["cricket","mountain","diamond","certificates","software","huminity"]

print("welcome to password guessing game")
print("difficulty level:easy,medium or hard")

level=input("Enter difficulty: ").lower()

if level == 'easy':
    secret=random.choice(easy_words)

elif level == 'medium':
    secret=random.choice(medium_words)

elif level == 'hard':
    secret=random.choice(hard_words)

else:
    print("invalid level.defaulting easy level")
    secret=random.choice(easy_words)

attempt=0
print("\n Guess the secret password")

while True:
    guess=input("Enter your guess: ").lower()
    attempt +=1

    if guess == secret:
        print(f"congratulation ! you guessed it in {attempt} attempts")
        break

    hint=""

    for i in range(len(secret)):
        if i < len(guess) and guess [i] == secret[i]:
            hint += guess[i]
        
        else:
            hint += "_"
    
    print("hint: ",hint)

print("Game over !")