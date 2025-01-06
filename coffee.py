class CoffeeShop:
    
    
    def __init__(self):
        
        self.orders = []
        self.menu = {
            "espresso": 120.00,
            "americano": 198.99,
            "cappuccino": 249.60,
            "latte": 199.95,
            "mocha": 349.50,
        }
        
    def display_menu(self):
        
        print("\n Cofee Shop Menu")
        
        for item, price in self.menu.items():
            print(f"{item} : {price:.2f}")   # 2 decimal places
    
    def take_order(self):
        
        print("\n Taking Order")
        
        self.display_menu()
        
        while True:
            
            choice = input("What would you like to order? (or type done to finish): ").strip()
            
            if choice.lower() == "done":
                break
            
            elif choice in self.menu:
                self.orders.append(choice)
                
                print(f"Added {choice} to your order.")
                
            else:
                
                print("Please choose from the menu. ")
                
    def view_order(self):
        
        if not self.orders:
            print("You haven't ordered anything yet.")
            
        else:
            print("\n Your Orders:")
            
            total = 0
            
            for order in self.orders:
                
                price = self.menu[order]
                
                total += price
                
                print(f"{order} : {price:.2f}")
            
            print(f"Total: {total:.2f}")
            
    
    
    def remove_order(self):
        
        if not self.orders:
            print("You haven't ordered anything yet.")
            
            return
        
        self.view_order()
        
        cancel_item = input("What would you like to remove? ").strip()
        
        if cancel_item in self.orders:
            self.orders.remove(cancel_item)
            
            print(f"Removed {cancel_item} from your order.")
            
        else:
            print("Item not found in your order.")
            
            
    def confirm_order(self):            
            if not self.orders:
                print("You haven't ordered anything yet.")
                
                
            confirm = input("Confirm order? (yes/no): ").strip()
            
            if confirm.lower() == "yes":
                print("Order placed.")
                print("Your total is: ", sum(self.menu[item] for item in self.orders))
                self.orders = []
                
                
            elif confirm.lower() == "no":
                print("Order cancelled.")
                
                
            else:
                print("Please enter yes or no.")
    

    def run(self):
        
        while True:
            
            print("\nOptions:")
            
            print("1. Display Menu")
            
            print("2. Place Order")
            
            print("3. View Order")
            
            print("4. Remove Order")
            
            print("5. Confirm Order")
            
            print("6. Exit")
            
            
            choice = input("What would you like to do? ").strip()
            
            if choice == "1":
                self.display_menu() 
                
            elif choice == "2":
                self.take_order()   
                
            elif choice == "3":
                self.view_order()
                
            elif choice == "4":
                self.remove_order() 
                
            elif choice == "5":
                self.confirm_order()
                
            elif choice == "6":
                
                print("Thank you for visiting the coffee shop.")
                break
            
            else:
                print("Invalid input. Please try again.")
                
if __name__ == "__main__":
    shop = CoffeeShop()
    
    shop.run()
            
