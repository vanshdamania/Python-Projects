import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
GameImages = [rock, paper, scissors]

UserChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(GameImages[UserChoice])

ComputerChoice = random.randint(0, 2)
print("Computer chose:")
print(GameImages[ComputerChoice])

if UserChoice >= 3 or UserChoice < 0: 
  print("You typed an invalid number, you lose!") 
elif UserChoice == 0 and ComputerChoice == 2:
  print("You win!")
elif ComputerChoice == 0 and UserChoice == 2:
  print("You lose")
elif ComputerChoice > UserChoice:
  print("You lose")
elif UserChoice > ComputerChoice:
  print("You win!")
elif ComputerChoice == UserChoice:
  print("It's a draw")
