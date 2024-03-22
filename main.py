from dao.OrderProcessor import OrderProcessor
from entity.Product import Product
from entity.User import User
from exception import UserNotFound, OrderNotFound
class OrderManagement:
    def __init__(self):
        self.orderProcessor = OrderProcessor()

    def display_menu(self):
        print("\nOrder Management System")
        print("1. Create User")
        print("2. Create Product")
        print("3. Create Order")
        print("4. Cancel Order")
        print("5. Get All Products")
        print("6. Get Orders by User")
        print("7. Exit")

    def create_user(self):
        userId = int(input("Enter User ID: "))
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        role = input("Enter Role (Admin/User): ")
        user = User(userId, username, password, role)
        self.orderProcessor.createUser(user)

    def create_product(self):
        user_id = int(input("Enter User ID: "))
        user = User(user_id, None, None, None)
        product_id = int(input("Enter Product ID: "))
        productName = input("Enter Product Name: ")
        description = input("Enter Product Description: ")
        price = float(input("Enter Product Price: "))
        Quantity = int(input("Enter Product Quantity: "))
        productType = input("Enter Product Type (Electronics/Clothing): ")
        product = Product(product_id, productName, description, price, Quantity, productType)
        self.orderProcessor.createProduct(user, product)

    def create_order(self):
        userId = int(input("Enter User ID: "))
        products = []
        while True:
            productId = int(input("Enter Product ID (0 to finish): "))
            if productId == 0:
                break
            products.append(Product(productId, None, None, None, None, None))
        user = User(userId, None, None, None)
        self.orderProcessor.createOrder(user, products)

    def cancel_order(self):
        userId = int(input("Enter User ID: "))
        orderId = int(input("Enter Order ID: "))
        try:
            self.orderProcessor.cancelOrder(userId, orderId)
        except UserNotFound as e:
            print("User not found:", e)
        except OrderNotFound as e:
            print("Order not found:", e)
        except Exception as e:
            print("An error occurred:", e)

    def get_all_products(self):
        products = self.orderProcessor.getAllProducts()
        if products:
            print("All Products:")
            for product in products:
                print(product)
        else:
            print("No products found.")

    def get_orders_by_user(self):
        userId = int(input("Enter User ID: "))
        orders = self.orderProcessor.getOrderByUser(User(userId, None, None, None))
        if orders:
            print(f"All Orders for User ID {userId}:")
            for order in orders:
                print(order)
        else:
            print(f"No orders found for User ID {userId}.")

    def main(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == "1":
                self.create_user()
            elif choice == "2":
                self.create_product()
            elif choice == "3":
                self.create_order()
            elif choice == "4":
                self.cancel_order()
            elif choice == "5":
                self.get_all_products()
            elif choice == "6":
                self.get_orders_by_user()
            elif choice == "7":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    orderManagement = OrderManagement()
    orderManagement.main()
