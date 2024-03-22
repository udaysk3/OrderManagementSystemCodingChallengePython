# OrderManagementSystemCodingChallengePython

<h1>SQL Schemas</h1>
<p>
CREATE TABLE Products (
    productId INT PRIMARY KEY,
    productName NVARCHAR(255),
    description NVARCHAR(MAX),
    price FLOAT,
    quantityInStock INT,
    type NVARCHAR(50)
);
</p>
<br>

<p>
CREATE TABLE Users (
    userId INT PRIMARY KEY,
    username NVARCHAR(255),
    password NVARCHAR(255),
    role NVARCHAR(50) CHECK (role IN ('Admin', 'User'))
);
</p>
<br>
<p>
CREATE TABLE [Order] (
    OrderId INT IDENTITY(1,1) PRIMARY KEY,
    UserId INT,
    FOREIGN KEY (UserId) REFERENCES Users(UserId)
);
</p>
<br>

-- Create OrderProduct table to represent the many-to-many relationship between Order and Product
<p>
CREATE TABLE OrderProduct (
    OrderId INT,
    ProductId INT,
    Quantity INT,
    PRIMARY KEY (OrderId, ProductId),
    FOREIGN KEY (OrderId) REFERENCES [Order](OrderId),
    FOREIGN KEY (ProductId) REFERENCES Products(ProductId)
);
</p>
<br>

SELECT * FROM USERS;
<br>
SELECT * FROM Products; <br>
SELECT * FROM [Order]; <br>
SELECT * FROM [OrderProduct]; <br>

<h3>Reference Screenshots</h3>
1: Adding User
<br>

![image](https://github.com/udaysk3/OrderManagementSystemCodingChallengePython/assets/75845600/c7473257-e403-464c-83a9-f80ac3c07b3f)
![image](https://github.com/udaysk3/OrderManagementSystemCodingChallengePython/assets/75845600/6fdb65c9-ad50-4d09-adef-72ac58d25964)

2: Adding Product <br>
![image](https://github.com/udaysk3/OrderManagementSystemCodingChallengePython/assets/75845600/26018ba5-1c9d-4974-acc2-b2db4e282c4c)
![image](https://github.com/udaysk3/OrderManagementSystemCodingChallengePython/assets/75845600/7f36e834-ae67-4abe-9ce2-003bdb4fdb19)

3: Create Order <br>
![image](https://github.com/udaysk3/OrderManagementSystemCodingChallengePython/assets/75845600/9a2c67b1-e3fd-414e-b6fb-e428c350567c)
![image](https://github.com/udaysk3/OrderManagementSystemCodingChallengePython/assets/75845600/c5d83b5a-784f-4146-9161-c00e82c0f268)


4: Get All Products <br>
![image](https://github.com/udaysk3/OrderManagementSystemCodingChallengePython/assets/75845600/9547532e-6110-44b9-98bf-09bb8c93bb00)
![image](https://github.com/udaysk3/OrderManagementSystemCodingChallengePython/assets/75845600/7954749d-42fd-41c1-8744-58d63df4d3d1)

5: Get Orders by User <br>
![image](https://github.com/udaysk3/OrderManagementSystemCodingChallengePython/assets/75845600/68d03b88-cc9c-42fe-bd8f-8504293a8b43)

6: Cancel Order <br>
![image](https://github.com/udaysk3/OrderManagementSystemCodingChallengePython/assets/75845600/40162699-50c7-4dde-9a17-d5de4156aef3)

7: User Not Found Exception <br>
![image](https://github.com/udaysk3/OrderManagementSystemCodingChallengePython/assets/75845600/9f853c25-4f7d-4d91-bf57-0bd5f4b4a4c8)

8: Order Not Found Exception <br>
![image](https://github.com/udaysk3/OrderManagementSystemCodingChallengePython/assets/75845600/8daddacb-a7fe-4057-a5a8-78abffd1faf2)



