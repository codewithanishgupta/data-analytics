-- SELECT *  FROM orders; 

-- UPDATE orders
-- SET order_status = 'Delivered'
-- WHERE order_id = 10


-- UPDATE orders
-- SET discount_percent = 10,
-- 	rating = 4
-- WHERE customer_name ='Neha Verma' AND order_id = 2;

-- SELECT * FROM orders

-- SET SQL_SAFE_UPDATES = 0 ;
-- UPDATE orders
-- SET order_status = 'Cancelled'
-- WHERE order_status = 'Pending';

-- SELECT * FROM orders

-- UPDATE orders
-- SET discount_percent = 20
-- WHERE category = 'Electronics' AND price_per_unit > 30000;


SELECT *
FROM orders
WHERE order_status = 'Pending';