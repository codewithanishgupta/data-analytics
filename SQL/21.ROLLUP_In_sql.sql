USE ecom;

-- SELECT * FROM orders;

-- DELETE FROM orders WHERE order_id = 13;

-- SELECT city , category, SUM(quantity * price_per_unit) as Total_sales
-- FROM orders
-- GROUP BY city , category WITH ROLLUP;


-- SELECT category,
--        COUNT(*) AS total_orders
-- FROM orders
-- GROUP BY category WITH ROLLUP;


SELECT
    city,
    category,
    SUM(quantity * price_per_unit) AS total_sales
FROM orders
GROUP BY city, category WITH ROLLUP;