import random

print("Welcome to Rock, Paper, Scissors!")

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: "))

rock = 0
paper = 1
scissors = 2

overall = [rock, paper, scissors]

Computer_choice = random.choice(overall)

if user_choice == 0:
    print(''' Your Choice: 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)''')

elif user_choice == 1:
    print(''' Your Choice:   
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')

elif user_choice == 2:
    print(''' Your Choice:
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

else:
    print("Invalid Input!")

if Computer_choice == rock:
    print(''' Computer's Choice: 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)''')

elif Computer_choice == paper:
    print(''' Computer's Choice:   
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')

else:
    print(''' Computer's Choice:
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

if user_choice == Computer_choice:
    print("It's a draw!")

elif user_choice == rock and Computer_choice == paper:
    print("You lose!")

elif user_choice == rock and Computer_choice == scissors:
    print("You win!")

elif user_choice == paper and Computer_choice == rock:
    print("You win!")

elif user_choice == paper and Computer_choice == scissors:
    print("You lose!")

elif user_choice == scissors and Computer_choice == paper:
    print("You win!")

elif user_choice == scissors and Computer_choice == rock:
    print("You lose!")

else:
    print("Game Over!")

print("\n🎮 Thanks for playing Rock, Paper, Scissors!")
