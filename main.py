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

# Write your code below this line 👇
game_images = [rock, paper, scissors]
game_on = True
import random

while game_on:
    your_choice = int(input("What do you choose? Type 0 for Rock,1 for Paper or 2 for Scissors\n"))
    if 0 < your_choice < 3:
        print(game_images[your_choice])
    else:
        print("You entered an invalid number!!")
        game_on = False

    computer_choice = random.randint(0, 2)
    print(f"Computer chooses:")
    print(game_images[computer_choice])

    if your_choice == 0 and computer_choice == 2:
        print("You win!!")
    elif your_choice == 2 and computer_choice == 1:
        print("You win")
    elif your_choice == computer_choice:
        print("Its a draw")
    elif your_choice == 0 and computer_choice == 1:
        print("You win")
    else:
        print("You lose")

    play_again = input("Do you want to play again? Yes or no : ").lower()
    if play_again == "yes":
        game_on = True
    else:
        game_on = False
