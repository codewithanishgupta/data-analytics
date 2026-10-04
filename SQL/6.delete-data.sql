SELECT * FROM orders;

-- DELETE FROM orders
-- WHERE order_id = 5;

-- DELETE FROM orders
-- WHERE order_status = 'Cancelled';

-- DELETE FROM orders
-- WHERE order_date < '2025-01-10';

SELECT *
FROM orders
WHERE order_status = 'Cancelled';