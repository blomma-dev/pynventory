from database import create_table
from functions import add_item, list_items, list_commands, available_commands, del_item


def main():
    
    # making sure the table exists before program starts
    create_table()

    print("Welcome to Pynventory!\n")
    print("Type \"help\" to see available commands.\n")

    # running the program until user chooses exit
    while True:
        command = input("Enter command: ").strip().lower()

        # running add command
        if command == "add":
            add_item()

        # running list command
        elif command == "list":
            list_items()

        # showing available commands
        elif command == "help":
            print(*available_commands, sep=", ")
            print()

        # closing the program
        elif command == "exit":
            print("Exiting Pynventory.")
            break

        # deleting product by ID
        elif command == "del":
            del_item()

        # placeholder for future modify command
        elif command == "modify":
            print("Modify function not implemented yet.\n")

        # showing help if command is invalid
        else:
            list_commands()


main()