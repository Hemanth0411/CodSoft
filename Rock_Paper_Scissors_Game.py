#TASK - 4
#Rock-Paper-Scissors Game

import random

game={
    1:"Rock",
    2:"Paper",
    3:"Scissors"
}

def decision(user_choice, computer_choice):
  if user_choice == computer_choice:
    return "It's a tie."

  elif (game[user_choice] == "Rock" and game[computer_choice] == "Paper") or\
   (game[user_choice] == "Paper" and game[computer_choice] == "Scissors") or\
    (game[user_choice] == "Scissors" and game[computer_choice] == "Rock"):
    return "You Lose!"

  else:
    return "You Win!"

user_score=0
computer_score=0
yes = True
print("Welcome to Rock-Paper-Scissors Game!!")

while yes:
  while True:
    print("\n1.Rock\n2.Paper\n3.Scissors")

    try:
      user_choice=int(input("Your Choice: "))

      if user_choice in [1,2,3]:
        break

      else:
        print("Choose from the given options!\n")
        continue

    except:
      print("Invalid Input! Try Again\n")
      continue

  computer_choice = random.randint(1,3)

  result=decision(user_choice, computer_choice)

  print(f"Your Choice: {game[user_choice]} & Computer's Choice: {game[computer_choice]}")
  print("\n",result)

  if "Lose" in result:
    computer_score+=1
  elif "Win" in result:
    user_score+=1

  print(f"\nYour Score: {user_score} \nComputer's Score: {computer_score}")

  ans=input("\nDo you wish to play again?(y/n): ").lower()

  if ans!='y':
    print("Thanks for playing!")
    yes=False

