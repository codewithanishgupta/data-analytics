use ecom;

-- SELECT * FROM orders;


-- ____COUNT_____
-- SELECT COUNT(*) 
-- FROM orders;

-- __SUM__
-- SELECT SUM(price_per_unit * quantity) AS total_revenue
-- FROM orders;

-- ___AVG____
-- SELECT AVG(price_per_unit)
-- FROM orders;

-- ___MIN and MAX__
-- SELECT MIN(price_per_unit) , MAX(price_per_unit)
-- FROM orders;

-- ___Scalar Functions___

-- __ROUND__
-- SELECT customer_name, ROUND(price_per_unit, 0)
-- FROM orders;

-- __UPPER and LOWER__
-- SELECT UPPER(customer_name), LOWER(city)
-- FROM orders;

-- __LENGTH__
-- SELECT customer_name , LENGTH(customer_name)
-- FROM orders;

-- __Date Functions__
-- _____CURRENT_DATE___
-- SELECT CURRENT_DATE;


-- __DATEDIFF__
-- SELECT order_id, DATEDIFF(delivery_date, order_date) AS delivery_days
-- FROM orders;

-- __Using Functions with WHERE__	
-- SELECT *
-- FROM orders
-- WHERE YEAR(order_date) = 2025;
