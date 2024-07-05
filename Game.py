import random

SCORE = 0
LIFE = 5

print("__________Welcome to Rock, Paper, Scissors________")

games = ['r', 'p', 's']

while LIFE != 0:
    choice = input("Enter your Choice? r = 'Rock', p = 'Paper', s = 'Scissors': ").lower()
    if choice not in games:
        print("Invalid choice. Please choose again.")
        continue

    AI = random.choice(games)

    if AI == choice:
        print(f"AI chose: {AI}")
        print("It's a tie!")
    elif (AI == 'p' and choice == 'r') or (AI == 'r' and choice == 's') or (AI == 's' and choice == 'p'):
        print(f"AI chose: {AI}")
        LIFE -= 1
        print(f"You LOSE! \nYour Score is = '{SCORE}' \nLIFE = '{LIFE}'")
    else:
        print(f"AI chose: {AI}")
        SCORE += 1
        print(f"You WON! \nYour Score is = '{SCORE}' \nLIFE = '{LIFE}'")

print("Game Over")
print(f"Final Score: {SCORE}")
