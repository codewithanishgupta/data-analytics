-- SELECT * FROM orders; 

-- SELECT * FROM orders WHERE order_status = 'Delivered';
-- SELECT customer_name,city,product FROM orders;

-- SELECT customer_name, product, price_per_unit
-- FROM orders
-- WHERE price_per_unit > 5000;

-- SELECT *
-- FROM orders
-- WHERE delivery_date IS NULL;

-- SELECT *
-- FROM orders
-- WHERE city = 'Delhi' AND order_status = 'Delivered';

SELECT customer_name, order_date, price_per_unit
FROM orders
ORDER BY order_date DESC;
