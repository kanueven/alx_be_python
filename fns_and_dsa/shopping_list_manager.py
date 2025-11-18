def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

#view shopping list
def view_list(shopping_list):
    if not shopping_list:
        print("Your shopping list is empty.")
    else:
        print("this is your shopping list:")
        for i,item in enumerate(shopping_list,start=1):
            print(f"{i}. {item}")

#add item to shopping list
def add_item(shopping_list):
    item = input("Enter the item to add:")
    shopping_list.append(item)
    print(f"{item} has been added to the shopping list.")
#remove item from shopping list
def remove_item(shopping_list):
    item = input("Enter the item you want to remove:")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} has been removed from the shopping list.")
    else:
        print(f"{item} is not in the shopping list.")

def main():
    # Initialize an empty shopping list
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_item(shopping_list)
        elif choice == "2":
            remove_item(shopping_list)
        elif choice == "3":
            view_list(shopping_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
#Run the functions
if __name__ == "__main__":
  main()