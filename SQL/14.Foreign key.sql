use ecom;

-- ALTER TABLE orders
-- ADD COLUMN seller_id INT;

-- ALTER TABLE orders
-- ADD CONSTRAINT fk_orders_seller
-- FOREIGN KEY (seller_id)
-- REFERENCES sellers(seller_id);


-- INSERT INTO orders (seller_id, product, quantity, price_per_unit)
-- VALUES (1, 'Laptop', 1, 65000);

-- INSERT INTO orders (seller_id, product, quantity, price_per_unit)
-- VALUES (999, 'Laptop', 1, 65000);


DELETE FROM sellers
WHERE seller_id = 1;

SELECT * FROM orders;