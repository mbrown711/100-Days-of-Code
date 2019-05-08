USE test_db;

CREATE TABLE IF NOT EXISTS NameTable (
            id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(20) NOT NULL,
            surname VARCHAR(20) NOT NULL,
            age INT NOT NULL
);

INSERT INTO NameTable VALUES (1, 'Bruce', 'Scott', 65);
INSERT INTO NameTable VALUES (2, 'John', 'Doe', 40);
INSERT INTO NameTable VALUES (3, 'Jane', 'Doe', 35);

DESC NameTable;
SELECT * FROM NameTable;