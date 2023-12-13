#TASK-6
contacts={}
def add_contact():
  name=input("Enter name: ")
  phone_number=input("Enter phone number: ")
  email=input("Enter E-mail: ")
  address=input("Enter Address: ")

  contact={
    'Name':name,
    'Phone Number' : phone_number,
    'Email' : email,
    'Address' : address}
  contacts[name]=contact
  print(f"Contact of {name} added successfully.\n")

def view_contact_list():
  pass

def search_contact():
  pass

def update_contact():
  pass

def delete_contact():
  pass 

def main():  
  while True:
    print("\n1.Add Contacts")
    print("2.View Contact List.")
    print("3.Search contact List")
    print("4.Update Contact")
    print("5.Delete Contact")
    print("6.Exit")
    choice=int(input("Enter your choice(1-6): "))

    if choice == 1:
      add_contact()
    elif choice == 2:
      view_contact_list()
    elif choice == 3:
      search_contact()
    elif choice == 4:
      update_contact()
    elif choice == 5:
      delete_contact()
    elif choice == 6:
      break

if __name__=='__main__':
  main()
