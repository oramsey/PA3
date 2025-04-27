CREATE DATABASE IF NOT EXISTS ecommerce_db;
use ecommerce_db;


CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    manufacturer_name VARCHAR(255),
    price DECIMAL(10, 2) NOT NULL,
    inventory_count INT NOT NULL
);

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    preferences VARCHAR(20)
);

CREATE TABLE products_bought (
    purchase_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    product_id INT,
    username VARCHAR(255),
    product_name VARCHAR(255),
    quantity INT NOT NULL,
    date_of_purchase DATE,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE ON UPDATE CASCADE
);
