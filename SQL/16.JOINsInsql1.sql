use ecom;

-- UPDATE orders SET seller_id =NULL WHERE order_id IN (1,9,14);

-- SELECT 
-- o.order_id, o.product, o.city AS customer_city,
-- s.seller_name
-- FROM orders o 
-- LEFT JOIN sellers s 
-- ON o.seller_id = s.seller_id
-- WHERE o.order_status = 'Delivered';

SELECT 
    s.seller_name,
    COUNT(o.order_id) AS total_orders
FROM sellers s
LEFT JOIN orders o
ON s.seller_id = o.seller_id
GROUP BY s.seller_name;

-- select * from orders
