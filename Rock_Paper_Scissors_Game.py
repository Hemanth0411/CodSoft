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
    return "You lose!"
  else:
    return "You Win!"


print("1.Rock\n2.Paper\n3.Scissors")
user_choice=int(input("Your Choice: "))

computer_choice = random.randint(1,3)
result=decision(user_choice, computer_choice)
print(f"Your Choice: {game[user_choice]} & Computer Choice: {game[computer_choice]}")
print(result)