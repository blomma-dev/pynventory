from database import create_table
from helpers import main_show_help, list_commands
from db_operations import (
    add_item,
    del_item,
    list_items,
    modify_item,
)

def main():
    create_table()

    print("Welcome to Pynventory!\n")
    print('Type "help" to see available commands.\n')
    try:
        while True:
            command = input("Enter command: ").strip().lower()

            if command == "add":
                add_item()
            elif command == "list":
                list_items()
            elif command == "help":
                main_show_help()
            elif command == "exit":
                print("Exiting Pynventory.")
                break
            elif command == "del":
                del_item()
            elif command == "mod":
                modify_item()
            else:
                list_commands()
    except KeyboardInterrupt:
        print("\nExiting Pynventory.")

if __name__ == "__main__":
    main()
