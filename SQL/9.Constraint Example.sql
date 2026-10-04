-- USE ecom;

-- CREATE TABLE employees (
-- 	emp_id INT PRIMARY KEY AUTO_INCREMENT,
-- 	email VARCHAR(150) UNIQUE,
-- 	name VARCHAR(100) NOT NULL,
-- 	age INT CHECK (age >= 18),
-- 	department VARCHAR(50) DEFAULT 'General',
-- 	salary DECIMAL(10,2) CHECK (salary > 0),
-- 	join_date DATE DEFAULT (CURRENT_DATE)
-- );

-- UNIQUE Constraint Example 
-- INSERT INTO employees (email, name, age, salary)
-- VALUES ('amit@company.com', 'Amit Sharma', 25, 45000);

-- NOT NULL Constraint Example 
-- INSERT INTO employees (email, age, salary)
-- VALUES ('neha@company.com', 24, 40000);

-- CHECK Constraint Example 
-- INSERT INTO employees (email, name, age, salary)
-- VALUES ('rahul@company.com', 'Rahul Khan', 16, 30000);

-- DEFAULT Constraint Example
-- INSERT INTO employees (email, name, age, salary)
-- VALUES ('pooja@company.com', 'Pooja Nair', 26, 50000);

 
SELECT * FROM employees; 