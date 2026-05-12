from pynventory.database import create_table
from pynventory.db_operations import (
    add_item,
    delete_item,
    list_items,
    modify_item,
    search_brand_or_product,
)
from pynventory.helpers import list_commands, main_help_dialog


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
            elif command == "del":
                delete_item()
            elif command == "mod":
                modify_item()
            elif command == "search":
                search_brand_or_product()
            elif command == "help":
                main_help_dialog()
            elif command == "exit":
                print("Exiting Pynventory.")
                break
            else:
                list_commands()
    except KeyboardInterrupt:
        print("\nExiting Pynventory.")


if __name__ == "__main__":
    main()
