CREATE DATABASE IF NOT EXISTS test;
USE test;
CREATE TABLE IF NOT EXISTS TestTable (
    id INT PRIMARY KEY,
    value VARCHAR(30) NOT NULL
);
INSERT INTO TestTable VALUES (01, "Hello");
INSERT INTO TestTable VALUES (02, "World");
INSERT INTO TestTable VALUES (03, ":)");
INSERT INTO TestTable VALUES (04, "wooooo");