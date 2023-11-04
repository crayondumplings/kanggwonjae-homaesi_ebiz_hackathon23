SELECT Customers.first_name, Customers.last_name, Orders.item, Orders.amount
FROM Customers
JOIN Orders ON Customers.customer_id = Orders.customer_id;
/*
Customers 테이블의 "first_name", Customers 테이블의 "last_name", Orders 테이블의 "item", Orders 테이블의 "amount" 칼럼을 출력한다.(SELECT Customers.first_name, Customers.last_name, Orders.item, Orders.amount)
"Customers" 테이블에서(FROM Customers)
customers_id가 같은 조건으로 "Orders" 테이블을 앞선 테이블과 합쳐서(JOIN Orders ON Customers.customer_id = Orders.customer_id)
*/
