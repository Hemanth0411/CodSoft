#TASK - 2
#CALCULATOR
  

choice=0

while True:
  if choice==5:
    break
  
  try:
    num1=float(input("\nEnter the first number: "))
    num2=float(input("Enter the second number: "))
  except:
    print("Invalid Input! Please enter a number.")
    continue
  
  while True:
    try:
      print("\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
      choice=int(input("Enter your choice: "))
      if choice == 1:
        print(f"{num1} + {num2} = {num1+num2}")  
      elif choice == 2:
        print(f"{num1} - {num2} = {num1-num2}")  
      elif choice == 3:
        print(f"{num1} * {num2} = {num1*num2}")  
      elif choice == 4:
        print(f"{num1} / {num2} = {num1/num2}")
      else:
        print("Invalid Choice. Please enter a number between 1-4. ")
        continue
      ch=input("\nWould you like to continue? (y/n): ").lower()
      if ch!='y':choice=5
      break
    except:
      print("Invalid Choice. Please choose a number between 1-4. ")
      continue
