CREATE DATABASE IF NOT EXISTS cafe;
USE cafe;

CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    drink VARCHAR(50),
    qty INT,
    price DECIMAL(5,2),
    branch VARCHAR(50),
    payment_type VARCHAR(20),
    datetime DATETIME
);
