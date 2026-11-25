USE ecom;

-- CREATE VIEW delevered_orders AS
-- SELECT order_id,
-- 		customer_name,
--         city,
--         product,
--         price_per_unit,
--         order_date
-- FROM orders
-- WHERE order_status = 'Delivered';


-- SELECT *
-- FROM delevered_orders;

-- UPDATE delevered_orders
-- SET price_per_unit = price_per_unit + 501
-- WHERE order_id = 1;

-- SELECT *
-- FROM delevered_orders;

DROP VIEW delevered_orders;
