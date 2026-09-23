

# Program Name: Assignment1.py
# Course: IT3883/Section W01
# Student Name: Komi Sowu
# Assignment Number: Lab 1
# Due Date: 09/22/2026
# Purpose: This program displays a menu that allows the user
#          to append data to an input buffer, clear the buffer, display
#          the current buffer contents, or exit the program.
# Resources Used: Course materials, Python documentation, and class notes.


def display_menu():
    """Prints the menu options."""
    print("\n" + "=" * 40)
    print("         MAIN MENU         ")
    print("=" * 40)
    print("1. Append data to the input buffer")
    print("2. Clear the input buffer")
    print("3. Display the input buffer")
    print("4. Exit the program")
    print("=" * 40)


def main():
    # Initialize an empty string to act as the input buffer
    input_buffer = ""

    # Loop continuously until the user chooses to exit
    while True:

        # Display the main menu
        display_menu()

        # Prompt the user to enter their choice
        choice = input("Enter your choice (1-4): ").strip()

        # Option 1: Append data to the buffer
        if choice == "1":
            user_text = input("Enter the string to append: ")

            # Append the new string to the existing buffer
            input_buffer += user_text

            print("Data appended successfully.")

        # Option 2: Clear the input buffer
        elif choice == "2":

            # Reset the buffer to an empty string
            input_buffer = ""

            print("Input buffer cleared.")

        # Option 3: Display the input buffer
        elif choice == "3":

            # Check if the buffer has any content
            if input_buffer:
                print(f"\nCurrent Buffer Content: '{input_buffer}'")
            else:
                print("\nThe buffer is currently empty.")

        # Option 4: Exit the program
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break

        # Handle an invalid menu selection
        else:
            print("Invalid selection. Please enter a number from 1 to 4.")


# Start the program
if __name__ == "__main__":
    main()
    
