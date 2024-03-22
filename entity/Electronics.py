from .Product import Product

class Electronics(Product):
    def __init__(self, productId, productName, description, price, quantityInStock, type, brand, warrantyPeriod):
        super().__init__(productId, productName, description, price, quantityInStock, type)
        self.brand = brand
        self.warrantyPeriod = warrantyPeriod

    # Getters and setters
    def getBrand(self):
        return self.brand

    def setBrand(self, brand):
        self.brand = brand

    def getWarrantyPeriod(self):
        return self.warrantyPeriod

    def setWarrantyPeriod(self, warrantyPeriod):
        self.warrantyPeriod = warrantyPeriod
