#!/usr/bin/env python3

import csv

FILENAME = "contacts.csv"

def write_contacts(contacts):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(contacts)

def read_contacts():
    contacts = []
    with open(FILENAME, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            contacts.append(row)
    return contacts

def list_contacts(contacts):
    for i in range(len(contacts)):
        contact = contacts[i]
        print(str(i+1) + ". " + contact[0])
    print()

def view_contact(contacts):
    index= int(input("Number: "))
    if index < 1 or index > len(contacts):
        print("This value does not exist. Please enter an existing value.\n")
    else:
        contact = contacts.pop(index)
        print(contact[0] + ", "+ contact[1] + ", "+ contact[2])
    print()

def add_contact(contacts):
    name = input("Name: ")
    email = input("Email: ")
    phone_number=input("Phone number: ")
    contact = []
    contact.append(name)
    contact.append(email)
    contact.append(phone_number)
    contacts.append(contact)
    write_contacts(contacts)
    print(name + " was added.\n")

def delete_contact(contacts):
    index = int(input("Number: "))
    if index < 1 or index > len(contacts):
        print("This value does not exist. Please enter an existing value.\n")
    else:
        contact = contacts.pop(index - 1)
        write_contacts(contacts)
        print(contact[0] + " was deleted.\n")

def display_menu():
    print("Contact Manager")
    print()
    print("COMMAND MENU")
    print("list - Display all contacts")
    print("view - view a contact")
    print("add - Add a contact")
    print("del - Delete a contact")
    print("exit - Exit program")
    print()

def main():
    display_menu()
    contacts = read_contacts()
    while True:
        command = input("Command: ")
        if command.lower()== "list":
            list_contacts(contacts)
        elif command.lower()=="view":
            view_contact(contacts)
        elif command.lower()=="add":
            add_contact(contacts)
        elif command.lower()=="del":
            delete_contact(contacts)
        elif command.lower()=="exit":
            break
        else:
            print("This is not a valid command. Please enter a valid command.\n")
    print("Bye!")

if __name__ == "__main__":
    main()
    
    
