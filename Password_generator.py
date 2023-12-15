import random 
import string

def gen_pass(length, complexity):
  characters=""
  password=""
  if "uppercase" in complexity:
    characters+=string.ascii_uppercase
  if "lowercase" in complexity:
    characters+=string.ascii_lowercase
  if "digit" in complexity:
    characters+=string.digits
  if "special" in complexity:
    characters+=string.punctuation
  if characters=="":
    print("\nChoose atleast one option!\n")
    return
  password="".join(random.choice(characters) for i in range(length))
  return password

try:
  length=int(input("\nSpecify the length of the password to generate: "))
except:
  print("Password length must be a number and greater than zero!")
while True:
  complexity_options=['uppercase', 'lowercase', 'digit', 'special']
  selected_complexity=[]
  for opt in complexity_options:
    choice=input(f"Do you want to include {opt} characters? (y/n): ")
    if choice == 'y':
      selected_complexity.append(opt)
  password=gen_pass(length, selected_complexity)
  if password==None:
    continue
  else:
    print(f"Password: {password}")
    break
