use ecom;

-- SELECT * FROM orders;

-- INCRESING ORDER 
-- SELECT * FROM orders ORDER BY price_per_unit 

-- DESECNDING ORDER 
-- SELECT * FROM orders ORDER BY price_per_unit DESC;

-- -----SHORT BY DATE-------
-- SELECT order_id, customer_name, order_date
-- FROM orders
-- ORDER BY order_date DESC;

-- SHORTING MULTIPLE COLUMN......
-- SELECT * FROM orders
-- ORDER BY city ASC, price_per_unit DESC;


-- SELECT LIMITED ROW ....
-- SELECT * FROM orders LIMIT 5;


-- use ordered with limit...
-- SELECT customer_name, product, price_per_unit
-- FROM orders
-- ORDER BY price_per_unit DESC
-- LIMIT 3;


-- OFFSET WITH LIMIT.....
SELECT * FROM orders ORDER BY order_date 
LIMIT 5 OFFSET 5;