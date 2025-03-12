
from tabulate import tabulate
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
            self.country =  country
            self.code = code
            self.product = product
            self.cost = float(cost)
            self.quantity = int(quantity)
        
    def get_cost(self):
        total_cost = 0
        with open ("Capstone_project_4_OOP/inventory.txt", "r") as file:
            for line in file:
                fields = line.strip().split(",")
                cost = float(fields [3])
                total_cost += cost

                print(f"The total costs are equal to: {[total_cost]}")
        return total_cost

    def get_quantity(self):
        total_quantity = 0
        with open ("Capstone_project_4_OOP/inventory.txt", "r") as file:
            for line in file:
                fields = line.strip().split(",")
                quantity = int(fields [4])
                total_quantity += quantity

                print(f"The total quantity is equal to: {[total_quantity]}")
        return total_quantity

    def __str__(self):
        return (f"Shoe Details:\n"
                f"Country: {self.country}\n"
                f"Code: {self.code}\n"
                f"Product: {self.product}\n"
                f"Cost: {self.cost}\n"
                f"Quantity: {self.quantity}")

shoe_list = []
#==========Functions outside the class==============
def read_shoes_data():
    try:
        with open("Capstone_project_4_OOP/inventory.txt", "r") as file:
            #skip the first line
            next(file)

            for line in file:
                try:
                    country, code, product, cost, quantity = line.strip().split(",")
                    shoe_list.append(Shoe(country, code, product, float(cost), int(quantity)))
                except ValueError:
                    print(f"Skipped line due to incorrect format: {line.strip()}")

            # Create a list to tabulate show details
            shoes_data = []
            for shoe in shoe_list:
                shoes_data.append([shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity])
            
            # Print the table using tabulate for better readability
            headers = ["Country", "Code", "Product", "Cost", "Quantity"]
            print(tabulate(shoes_data, headers=headers, tablefmt="fancy_grid"))

    except FileNotFoundError:
        print("Error: File not found. Check the file path.")
    return shoe_list

def capture_shoes():
    print("Enter the following details of the new shoe:")

    country = input("Enter the country of origin:")
    code = input("Enter your product code:")
    product = input("Product name:")
    cost = float(input("Cost:"))
    quantity = int(input("Quantity:"))

    try:
        # New shoe object
        new_shoe = Shoe(country, code, product, cost, quantity)
        
        # Appending shoe list
        shoe_list.append(new_shoe)
        print("Shoe added successfully and added to the list")
    
    except ValueError:\
        print("Error: Invalid data entered")


def view_all():

    if not shoe_list:
        print("No shoe data available.")
        return

    # headers for table
    headers = ["Country", "Code", "Product", "Cost", "Quantity"]
    shoe_data = [[shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity] for shoe in shoe_list] 
    print(tabulate(shoe_data, headers=headers, tablefmt="fancy_grid"))


def re_stock():

    try:
        # Ensure 'shoes' is a list of Shoe objects
        if not shoe_list:
            print("No shoe data available.")
            return

        # Find the shoe with the lowest quantity
        lowest_shoe = min(shoe_list, key=lambda shoe: shoe.quantity)

        print(f"The shoe with the lowest quantity is: {lowest_shoe.product}")
        print(f"Quantity: {lowest_shoe.quantity}")
        print(f"Code: {lowest_shoe.code}")

        # Ask user if they want to restock
        restock_query = input("Would you like to restock this shoe? (yes/no): ")
        if restock_query.lower() == "yes":
            restock_quantity = int(input("How many units would you like to add to the existing stock>: "))
            lowest_shoe.quantity += restock_quantity
        else:
            print(f"No updates will be made for the stock of {lowest_shoe.code} ")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



def search_shoe():

    identify_shoe= input("Enter the shoe code: ")

    try:
        if not shoe_list:
            print("No shoe data available.")
            return

        # Filter the shoe data for the given code
        shoe_data = [
            [shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity]
            for shoe in shoe_list
            if shoe.code == identify_shoe
        ]

        if shoe_data:
            for shoe in shoe_data:
                print(f"Country: {shoe[0]}, Product: {shoe[2]}, Cost: {shoe[3]}, Quantity: {shoe[4]}")
        else:
            print("Shoe not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def value_per_item():

    shoe_data = [
        [shoe.code, shoe.product, shoe.cost, shoe.quantity, shoe.cost * shoe.quantity]
        for shoe in shoe_list
    ]
    
    # Headers for the table
    headers = ["Code", "Product", "Cost", "Quantity", "Value"]

    # Print the table
    print(tabulate(shoe_data, headers=headers, tablefmt="fancy_grid"))


def highest_qty():

    try:
        # Ensure 'shoes' is a list of Shoe objects
        if not shoe_list:
            print("No shoe data available.")
            return

        # Find the shoe with the highest quantity
        highest_shoe = max(shoe_list, key=lambda shoe: shoe.quantity)

        print(f"The shoe with the highest quantity is: {highest_shoe.product}")
        print(f"Quantity: {highest_shoe.quantity}")
        print(f"Code: {highest_shoe.code}")
        print(f"The shoe that will go on sale is for code: {highest_shoe.code} ,with the quantity of: {highest_shoe.product}")

    except FileNotFoundError:
        print("Error: File not found. Check the file path.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


#==========Main Menu=============

def main_menu():
    while True:
        print("\nShoe Inventory Management System")
        print("1. Read Shoes Data")
        print("2. Capture Shoes")
        print("3. View All Shoes")
        print("4. Re-stock")
        print("5. Search Shoe")
        print("6. Value Per Item")
        print("7. Highest Quantity")
        print("8. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            read_shoes_data()
        elif choice == "2":
            capture_shoes()
        elif choice == "3":
            view_all()
        elif choice == "4":
            re_stock()
        elif choice == "5":
            search_shoe()
        elif choice == "6":
            value_per_item()
        elif choice == "7":
            highest_qty()
        elif choice == "8":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the Main Menu
main_menu()
