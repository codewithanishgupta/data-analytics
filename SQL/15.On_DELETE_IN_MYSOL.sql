use ecom;

-- ALTER TABLE orders
-- ADD CONSTRAINT fk_orders_seller
-- FOREIGN KEY (seller_id)
-- REFERENCES sellers(seller_id);


-- ALTER TABLE orders
-- DROP FOREIGN KEY fk_orders_seller;

-- ALTER TABLE orders
-- ADD CONSTRAINT fk_orders_seller
-- FOREIGN KEY (seller_id)
-- REFERENCES sellers(seller_id)
-- ON DELETE CASCADE;

-- DELETE FROM sellers
-- WHERE seller_id = 3;

-- ALTER TABLE orders
-- MODIFY seller_id INT NULL;

-- ALTER TABLE orders
-- DROP FOREIGN KEY fk_orders_seller;

-- ALTER TABLE orders
-- ADD CONSTRAINT fk_orders_seller
-- FOREIGN KEY (seller_id)
-- REFERENCES sellers(seller_id)
-- ON DELETE SET NULL;


-- ALTER TABLE orders
-- DROP FOREIGN KEY fk_orders_seller;

-- ALTER TABLE orders
-- ADD CONSTRAINT fk_orders_seller
-- FOREIGN KEY (seller_id)
-- REFERENCES sellers(seller_id)
-- ON DELETE RESTRICT;

DELETE FROM sellers
WHERE seller_id = 5;

SELECT * FROM orders;