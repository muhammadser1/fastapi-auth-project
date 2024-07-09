CREATE DATABASE auth_db;

USE auth_db;
CREATE TABLE User (
    username VARCHAR(50) PRIMARY KEY,
    password_hash VARCHAR(255),
    email VARCHAR(100),
    role VARCHAR(100)
);


