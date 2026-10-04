USE ecom;
-- Add new column.....
-- Alter Table orders
-- ADD COLUMN delivery_parternar VARCHAR(50);

-- modify existing column...
-- ALTER TABLE orders
-- MODIFY price_per_unit DECIMAL(12,2);

-- Rename  the column name 
-- ALTER TABLE orders
-- RENAME COLUMN city to customer_city;

-- Droping column 
-- ALTER TABLE orders
-- DROP COLUMN rating;

-- Delete table data
-- DELETE FROM orders;

-- Droping a table alter
-- DROP TABLE 	ORDERS;

-- SELECT * FROM orders; 

DROP TABLE IF EXISTS orders;
