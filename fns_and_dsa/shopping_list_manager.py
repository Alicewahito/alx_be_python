def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # ✅ Defined as a list

    while True:
        display_menu()  # ✅ Function is called

        choice = input("Enter your choice: ")  # ✅ Input is captured

        if choice == '1':  # ✅ Choice is checked as a string
            item = input("Enter item to add: ")
            shopping_list.append(item)
            print(f"{item} added to the shopping list.")
        elif choice == '2':
            item = input("Enter item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} removed from the shopping list.")
            else:
                print(f"{item} not found in the shopping list.")
        elif choice == '3':
            print("Current Shopping List:")
            for item in shopping_list:
                print(f"- {item}")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
