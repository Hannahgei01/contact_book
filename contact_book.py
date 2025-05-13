import os

#simple contact class
class Contact:
  def __init__(self, name, number):
    self.name = name
    self.number = number

  def __str__(self):
    return f'Name: {self.name}, Number: {self.number}'

#empty dictionary
contacts = {}

#1. load contacts
def load_contacts(filename):
  if os.path.exists(filename):
    with open(filename, 'r') as f:
      for line in f:
        try:
          name, number = line.strip().split(",")
          contacts[name] = Contact(name, number)
        except ValueError:
          print("Error while loading the line:", line)

#2. save contacts
def save_contacts(filename):
  with open(filename, "w") as f:
    for contact in contacts.values():
      f.write(f'{contact.name}, {contact.number}\n')

#3. add contacts
def add_contacts():
  name = str(input("Input Name:"))
  number = input("Input Phone Number:")
  contacts[name] = Contact(name, number)
  print(f"{name} got added.")

#4. show contacts
def show_contacts():
  if contacts:
    for contact in contacts.values():
      print(contact)
  else:
    print("No contacts have been saved yet.")

#5. search contacts
def search_contacts():
  name = input("Which name do you want to search?")
  contact = contacts.get(name)
  if contact:
    print("Found.", contact)
  else:
    print(f"{name} not in contact book.")

#6. delete contact
def delete_contact(name):
  name = input("Input name of the contact you wish to delete: ").strip()
  if name in contacts:
    confirmation = input("Are you sure you want to delete {name}?(y/n)")
    if confirmation == "y":
      del contacts[name]
      print("Contact has been deleted.")
    else:
      print("Cancelled request.")
  else:
    print("Contact not found.")

#menu
def show_menu():
  print("\n --- Contact Book Menu ---")
  print("1. Add Contact")
  print("2. View all Contacts")
  print("3. Search Contact")
  print("4. Delete Contact")
  print("5. Close Contact Book")
  return int(input("Please choose one option (1-5): "))

#main
def main():
  filename = "contact_book.txt"
  load_contacts(filename)

  while True:
    selection = show_menu()

    if selection == 1:
      add_contacts()
    elif selection == 2:
      show_contacts()
    elif selection == 3:
      search_contacts()
    elif selection == 4:
      delete_contact(filename)
    elif selection == 5:
      save_contacts(filename)
      print("Contacts saved. Program will close.")
      break
    else: 
      print("Invalid input. Please insert option 1-5.")

if __name__ == "__main__":
  main()


