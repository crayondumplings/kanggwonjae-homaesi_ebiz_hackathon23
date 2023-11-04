SELECT Customers.first_name, Customers.last_name, Orders.item, Orders.amount
FROM Customers
JOIN Orders ON Customers.customer_id = Orders.customer_id;
