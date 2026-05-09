def show_menu(): # we use a function rather than multiple prints so this can be displayed over and over again.
    print("\nExpense Tracker")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Show total spending")
    print("4. Exit")

while True: # this creates an infinite loop that will keep showing the menu until the user chooses to exit.
        show_menu() # call the function to display the menu options
        choice = input("Choose an option: ")

        if choice == "1":
            print("Add expense selected")
        elif choice == "2":
            print("View expenses selected")
        elif choice == "3":
            print("Total spending selected")
        elif choice == "4":
            print("Goodbye!") 
            break # stop the while true loop and exit the program
        else: # otherwise keep asking for input until a valid option is chosen
            print("Invalid option. Please choose 1, 2, 3, or 4.")