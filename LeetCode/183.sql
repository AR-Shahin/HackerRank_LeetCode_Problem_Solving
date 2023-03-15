SELECT Customers.name as Customers
    FROM Customers
    WHERE Customers.id NOT IN (SELECT customerId from Orders)