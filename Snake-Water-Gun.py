import random

choices = ['s', 'w', 'g']
comp = random.choice(choices)

user = input("Enter s (snake), w (water), g (gun): ").lower().strip()

print("You chose:", user)
print("Computer chose:", comp)

if user == comp:
    print("ITS A DRAW")

elif (user == 's' and comp == 'w') or \
     (user == 'w' and comp == 'g') or \
     (user == 'g' and comp == 's'):
    print("YOU WIN HURRAYY !")

else:
    print("YOU LOSE ")