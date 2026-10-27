use ecom;

-- select * from orders
-- where city IN ('Delhi' , 'Mumbai' , 'Bangalore');

-- Select * From orders
-- where payment_mode NOT IN ('cash' , 'upi')


-- select * from orders 
-- where price_per_unit Between 1000 AND 5000;


-- SELECT * FROM orders
-- WHERE price_per_unit NOT BETWEEN 1000 AND 10000;


-- select * from orders
-- where customer_name like 'A%';


-- select * from orders
-- where product like '%table%';


-- select * from orders 
-- where city like 'D_lhi';


select * from orders
where category IN ('Electronics' , 'Furniture')
AND price_per_unit Not Between 5000 and 20000;