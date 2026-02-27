# Hotel Management System using OOPS

class Customer:
    def __init__(self, name, room_type, days):
        self.name = name
        self.room_type = room_type
        self.days = days
        self.rate = self.get_room_rate()
        self.bill = self.calculate_bill()

    def get_room_rate(self):
        room_rates = {
            "single": 1000,
            "double": 2000,
            "suite": 3500
        }
        return room_rates.get(self.room_type.lower(), 0)

    def calculate_bill(self):
        return self.rate * self.days

    def display_details(self):
        print("\n--- Customer Details ---")
        print(f"Name: {self.name}")
        print(f"Room Type: {self.room_type}")
        print(f"Days Stayed: {self.days}")
        print(f"Total Bill: ₹{self.bill}")
        print("-------------------------")


class HotelManagement:
    def __init__(self):
        self.customers = {}

    def add_customer(self):
        name = input("Enter Customer Name: ")
        room_type = input("Enter Room Type (Single/Double/Suite): ")
        days = int(input("Enter Number of Days: "))

        customer = Customer(name, room_type, days)
        self.customers[name] = customer

        print("Customer added successfully!\n")

    def view_customer(self):
        name = input("Enter Customer Name to View: ")
        if name in self.customers:
            self.customers[name].display_details()
        else:
            print("Customer not found!\n")

    def remove_customer(self):
        name = input("Enter Customer Name to Remove: ")
        if name in self.customers:
            del self.customers[name]
            print("Customer removed successfully!\n")
        else:
            print("Customer not found!\n")

    def show_all_customers(self):
        if not self.customers:
            print("No customers available.\n")
            return
        for customer in self.customers.values():
            customer.display_details()


def main():
    hotel = HotelManagement()

    while True:
        print("\n===== HOTEL MANAGEMENT SYSTEM =====")
        print("1. Add Customer")
        print("2. View Customer")
        print("3. Remove Customer")
        print("4. View All Customers")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            hotel.add_customer()
        elif choice == "2":
            hotel.view_customer()
        elif choice == "3":
            hotel.remove_customer()
        elif choice == "4":
            hotel.show_all_customers()
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Try again.\n")


if __name__ == "__main__":
    main()
