from .IOrderManagementRepository import IOrderManagementRepository
from exception.UserNotFound import UserNotFound
from exception.OrderNotFound import OrderNotFound
from util.DBConnUtil import DBConnUtil
from entity.User import User

class OrderProcessor(IOrderManagementRepository):
    def createOrder(self, user, products):
        try:
            connection = DBConnUtil.getDBConn()
            if connection:
                cursor = connection.cursor()
                cursor.execute("SELECT COUNT(*) FROM Users WHERE userId = ?", user.getUserId())
                user_count = cursor.fetchone()[0]
                if user_count == 0:
                    cursor.execute("INSERT INTO Users (userId, username, password, role) VALUES (?, ?, ?, ?)",
                                user.getUserId(), user.getUsername(), user.getPassword(), user.getRole())
                    connection.commit()
                    print("User created successfully.")
                    
                cursor.execute("INSERT INTO [Order] ( UserId) OUTPUT INSERTED.OrderId VALUES (?)", user.getUserId())
                
                order_id = cursor.fetchone()[0]
                print(order_id)
                order_product_data = [(order_id, product.getProductId()) for product in products]
                cursor.executemany("INSERT INTO OrderProduct (OrderId, ProductId) VALUES (?, ?)", order_product_data)
                connection.commit()
                print("Order created successfully.")
            else:
                print("Failed to connect to database.")
        except Exception as e:
            print("Error creating order:", e)
        finally:
            if connection:
                connection.close()

                
    def cancelOrder(self, userId, orderId):
        try:
            connection = DBConnUtil.getDBConn()
            if connection:
                cursor = connection.cursor()
                cursor.execute("SELECT COUNT(*) FROM Users WHERE userId = ?", userId)
                user_count = cursor.fetchone()[0]
                if user_count == 0:
                    raise UserNotFound(f"User with ID {userId} not found.")

                cursor.execute("SELECT COUNT(*) FROM [Order] WHERE userId = ? AND orderId = ?", userId, orderId)
                order_count = cursor.fetchone()[0]
                if order_count == 0:
                    raise OrderNotFound(f"Order with ID {orderId} not found for user {userId}.")
                cursor.execute("DELETE FROM [OrderProduct] WHERE orderId = ?", orderId)
                cursor.execute("DELETE FROM [Order] WHERE userId = ? AND orderId = ?", userId, orderId)
                connection.commit()
                print("Order cancelled successfully.")
            else:
                print("Failed to connect to database.")
        except UserNotFound as e:
            print("Error cancelling order:", e)
        except OrderNotFound as e:
            print("Error cancelling order:", e)
        except Exception as e:
            print("Error cancelling order:", e)
        finally:
            if connection:
                connection.close()

    def createProduct(self, user, product):
        try:
            connection = DBConnUtil.getDBConn()
            if connection:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM Users WHERE userId = ?", user.getUserId())
                user_data = cursor.fetchone()
                if user_data:
                    user = User(user_data[0], user_data[1], user_data[2], user_data[3])
                    if user.getRole() != "Admin":
                        print("Error: User is not an admin.")
                        return
                    
                    cursor.execute("INSERT INTO Products (productId, productName, description, price, quantityInStock, type) VALUES (?, ?, ?, ?,?,?)",
                            product.getProductId() ,product.getProductName(), product.getDescription(), product.getPrice(), product.getQuantityInStock(), product.getType()), 
                    connection.commit()
                    print("Product created successfully.")
                else:
                    print("User not found.")
                    return None
            else:
                print("Failed to connect to database.")
                
        except Exception as e:
            print("Error creating product:", e)
        finally:
            if connection:
                connection.close()

    def createUser(self, user):
        try:
            connection = DBConnUtil.getDBConn()
            if connection:
                cursor = connection.cursor()
                cursor.execute("SELECT COUNT(*) FROM Users WHERE userId = ?", user.getUserId())
                user_count = cursor.fetchone()[0]
                if user_count > 0:
                    print(f"User with ID {user.getUserId()} already exists.")
                    return
                cursor.execute("INSERT INTO Users (userId, username, password, role) VALUES (?, ?, ?, ?)",
                               user.getUserId(), user.getUsername(), user.getPassword(), user.getRole())
                connection.commit()
                print("User created successfully.")
            else:
                print("Failed to connect to database.")
        except Exception as e:
            print("Error creating user:", e)
        finally:
            if connection:
                connection.close()

    def getAllProducts(self):
        try:
            connection = DBConnUtil.getDBConn()
            if connection:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM Products")
                products = cursor.fetchall()
                return products
            else:
                print("Failed to connect to database.")
                return []
        except Exception as e:
            print("Error retrieving products:", e)
            return []
        finally:
            if connection:
                connection.close()

    def getOrderByUser(self, user):
        try:
            connection = DBConnUtil.getDBConn()
            if connection:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM [Order] WHERE userId = ?", user.getUserId())
                order = cursor.fetchall()
                return order
            else:
                print("Failed to connect to database.")
                return []
        except Exception as e:
            print("Error retrieving order:", e)
            return []
        finally:
            if connection:
                connection.close()