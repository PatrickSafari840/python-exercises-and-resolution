
# Here's a rewrite of the question for the list exercise:

# List Manipulation Program

# This code demonstrates working with lists in Python. It provides a menu-driven interface that allows you to:

# Add an element to a list.
# Delete an element from the list.
# View the current contents of the list.
# Clear the entire list.
# Exit the program.
# The program uses a loop to keep presenting the menu until you choose to exit. It also incorporates error handling to ensure you enter valid choices.




LIST = []
menu = """
1.Add an element to your list
2.Delete an element from your list
3.Display the elements of the list
4.Empty the entire list
5.Exit
"""
choice = ["1","2","3","4","5"]

while True:  # Loop to keep the program running until user exits
    user_choice = ""
    while user_choice not in choice:  # Loop to ensure valid user input
        user_choice = input(menu)
        if user_choice not in choice:
            print("Please choose a valid option!")

    if user_choice == "1":  # Add an element to the list
        element = input("Enter the element you want to add to your list: ")
        LIST.append(element)
        print(f"Element {element} has been added successfully.")
        print("-" * 100)
    elif user_choice == "2":  # Delete an element from the list
        element = input("Enter the element you want to delete from your list: ")
        if element not in LIST:
            print(f"Element {element} does not exist in your list.")
        else:
            LIST.remove(element)
            print(f"Element {element} has been deleted successfully.")
            print("-" * 100)
    elif user_choice == "3":  # Display the elements of the list
        if LIST:  # Check if list is empty
            for i, element in enumerate(LIST, 1):  # Enumerate to print index and element
                print(f"{i}. {element}")
            print("-" * 100)
        else:
            print("Your list is empty!")
    elif user_choice == "4":  # Empty the entire list
        LIST.clear()
        print("Your list has been emptied successfully.")
        print("-" * 100)
    elif user_choice == "5":  # Exit the program
        print("Thank you and goodbye!")
        print("-" * 100)
        break

print("-" * 100)  # Final separator
