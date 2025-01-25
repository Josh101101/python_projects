


class FoodDeliveryApp:
    
    def __init__(self):
        
        self.menu = {
            
            1 : {"name": "Palak paneer", "price": 10.99},
            
            2 : {"name": "Paneer butter masala", "price": 15.99},
            
            3 : {"name": "Paneer tikka masala", "price": 18.99},
            
            4 : {"name": "Paratha", "price": 14.99},
            
            5 : {"name": "Rajma chaval	", "price": 12.99},
            
            6 : {"name": "Chole bhature", "price": 16.99},
            
            7 : {"name": "Pav bhaji", "price": 13.99},
            
            8 : {"name": "Dosa", "price": 11.99},
            
            9 : {"name": "Idli sambhar", "price": 10.99},
            
            10 : {"name": "Vada pav", "price": 8.99}
            
            
            
        }
        
        self.cart = []
        
    def display_menu(self):
        
        print("\nMenu:")
        
        for key, value in self.menu.items():
            print(f"{key}. {value['name']} - ${value['price']: .2f}")
            
    def take_order(self):
        
        try:  
            self.display_menu()
            
            item = int(input("\nEnter the number of the item you would like to order: "))
            
            if item in self.menu:
                
                quantity = int(input("Enter the quantity: "))
                
                self.cart.append({
                    
                    "name": self.menu[item]["name"],
                    
                    "price": self.menu[item]["price"],
                    
                    "quantity": quantity
                    
                })
                
                print(f"{quantity} {self.menu[item]['name']} added to cart.")
                
            else:
                print("Invalid item number.")
            
        except ValueError:
            print("Invalid input. Enter a Valid Number.")
            
            
            
    def view_order(self):
        
        if not self.cart:
            print("Cart is empty.")
            
        else:
            print("\n Your Cart: ")
            
            total = 0
            
            for item in self.cart:
                
                price = item["price"] * item["quantity"]
                
                total += price
                
                print(f"{item['name']} x {item['quantity']} : ${price:.2f}")
                
                
            print(f"Total: ${total:.2f}")
            
    def place_order(self):
        
        if not self.cart:
            print("Cart is empty.")
            
        else:
            self.view_order()
            confirm = input("Would you like to place the order? (yes/no): ").strip().lower()
            
            if confirm == "yes":
                print("\n Your Order has been placed.")
                
                self.cart.clear()
                
            else:
                print("Order Cancelled.")
                
                
                
    def remove_order(self):
        
        if not self.cart:
            print("Cart is empty.")
            
        else:
            self.view_order()
            
            item = input("Enter the name of the item you would like to remove: ").strip().title()
            
            for i in self.cart:
                if i["name"] == item:
                    self.cart.remove(i)
                    print(f"{item} removed from cart.")
                    break
                
            else:
                print(f"{item} not found in cart.")
                
    
    
    def run(self):
        
        try:
            while True:
                print("\n --- Food Delivery App ---")
                print("1. Display Menu")
                print("2. Take Order")
                print("3. View Order")
                print("4. Place Order")
                print("5. Remove Order")
                print("6. Exit")
                
                choice = input("Enter your choice: ").strip()
                
                if choice == "1":
                    self.display_menu()
                    
                elif choice == "2":
                    self.take_order()
                    
                elif choice == "3":
                    self.view_order()
                    
                elif choice == "4":
                    self.place_order()
                    
                elif choice == "5":
                    self.remove_order()
                    
                elif choice == "6":
                    print("Thank you for using the app.")
                    break
                
                
                    
                else:
                    print("Invalid input. Please enter a valid choice.")
                
                
        except ValueError:
            print("Invalid input. Enter a valid number.")
            

if __name__ == "__main__":
    
    app = FoodDeliveryApp()
    
    app.run()
                
            
            
        