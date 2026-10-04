use ecom;
CREATE TABLE customer(
	customer_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_name VARCHAR(100),
    email VARCHAR(150),
    age INT,
    phone VARCHAR(15),
    is_active BOOLEAN,
    singup_date DATE,
    create_at DATETIME,
    total_spent DECIMAL(10,2)
);

ALTER TABLE customer RENAME TO clients;