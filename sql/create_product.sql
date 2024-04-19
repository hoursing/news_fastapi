select * from products;

CREATE TABLE products(
    id serial NOT NULL primary key,
    name character varying NOT NULL,
    price int NOT NULL   
);

ALTER TABLE products ADD COLUMN is_sale boolean DEFAULT false;
ALTER TABLE products ADD COLUMN inventory int DEFAULT 0;
ALTER TABLE products ADD COLUMN created_at TIMESTAMP with time zone DEFAULT NOW();

INSERT INTO products(name, price) VALUES('TV', 200);
INSERT INTO products(name, price) VALUES('DVD Player', 80);
INSERT INTO products(name, price) VALUES('Remote', 10);
INSERT INTO products(name, price) VALUES('Microphone', 30);

