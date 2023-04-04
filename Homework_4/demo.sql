CREATE TABLE tag (
    id SERIAL PRIMARY KEY,
    title VARCHAR(50)
);
CREATE TABLE seller (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50)
);
CREATE TABLE customer (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50)
);
CREATE TABLE product (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    price FLOAT NOT NULL,
    seller_id INT,
    CONSTRAINT seller_fk
    FOREIGN KEY (seller_id)
    REFERENCES seller(id)
    ON DELETE CASCADE
);

CREATE TABLE wishlist (
    id SERIAL PRIMARY KEY,
    customer_id INT UNIQUE,
    CONSTRAINT customer_fk
    FOREIGN KEY (customer_id)
    REFERENCES customer(id)
    ON DELETE CASCADE
);
CREATE TABLE review (
    id SERIAL PRIMARY KEY,
    rate INT,
    customer_id INT,
    product_id INT,
    CONSTRAINT customer_review_fk
    FOREIGN KEY (customer_id)
    REFERENCES customer(id),
    ON DELETE SET NULL
    CONSTRAINT product_review_fk2
    FOREIGN KEY (product_id)
    REFERENCES product(id)
    ON DELETE CASCADE
);
CREATE TABLE product_tags (
    id SERIAL PRIMARY KEY,
    product_id INT,
    tag_id INT,
    CONSTRAINT prod_id_fk
    FOREIGN KEY (product_id)
    REFERENCES product(id),
    CONSTRAINT tag_id_fk
    FOREIGN KEY (tag_id)
    REFERENCES tag(id)
);