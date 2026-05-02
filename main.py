from database import create_table
from functions import add_item, list_items, list_commands, available_commands, del_item, modify_item


def main():
    create_table()

    print("Welcome to Pynventory!\n")
    print('Type "help" to see available commands.\n')

    while True:
        command = input("Enter command: ").strip().lower()

        if command == "add":
            add_item()
        elif command == "list":
            list_items()
        elif command == "help":
            print(*available_commands, sep=", ")
            print()
        elif command == "exit":
            print("Exiting Pynventory.")
            break
        elif command == "del":
            del_item()
        elif command == "modify":
            modify_item()
        else:
            list_commands()


if __name__ == "__main__":
    main()