/* 
Ronald Rojas
CYBR410-T302
Prof. P. Haas
03/02/2023
 */

 -- Drop function if user already exists
DROP USER IF EXISTS 'root2'@'localhost';

-- Create the whatabook_user account and grant all privileges to the whatabook database 
CREATE USER 'root2'@'localhost' IDENTIFIED WITH mysql_native_password BY 'Wh1te###gv7b';

-- Grant all privileges to database user named whatabook_user on localhost 
GRANT ALL PRIVILEGES ON whatabook.* TO'root2'@'localhost';

-- Drop contstraints if they exist
ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

-- Drop tables if they exist
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;

/*
    Create the table(s)
*/
CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);

/*
    Insert store information 
*/
INSERT INTO store(locale)
    VALUES('972 5th Ave, New York, NY 10075');

/*
    Insert book information 
*/
INSERT INTO book(book_name, author, details)
    VALUES('In Search of lost Time', 'Marcel Proust', 'Swanns Way');

INSERT INTO book(book_name, author, details)
    VALUES('Don Quijote', 'Miguel de Cervantes', 'A Book of Chivalry');

INSERT INTO book(book_name, author)
    VALUES('Hamlet', 'William Shakespeare');

INSERT INTO book(book_name, author)
    VALUES('Madame Bovary', 'Gustave Flaubert');

INSERT INTO book(book_name, author)
    VALUES('Dune: Deluxe Edition', 'Frank Herbert');

INSERT INTO book(book_name, author)
    VALUES("Charlotee's Web", 'E.B. White');

INSERT INTO book(book_name, author)
    VALUES('The Great Gatsby', 'F. Scott Fitzgerald');

INSERT INTO book(book_name, author)
    VALUES('The Lion, the Witch, and the Wardrobe', 'C.S. Lewis');

INSERT INTO book(book_name, author)
    VALUES('The Catcher and the Rye', 'J.D. Salinger');

/*
    Insert the users
*/ 
INSERT INTO user(first_name, last_name) 
    VALUES('Paul', 'VanDyke');

INSERT INTO user(first_name, last_name)
    VALUES('Armin van', 'Buren');

INSERT INTO user(first_name, last_name)
    VALUES('Brian', 'Transeau');

/*
    Insert wishlist records 
*/
INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Paul'), 
        (SELECT book_id FROM book WHERE book_name = 'Dune: Deluxe Edition')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Brian'),
        (SELECT book_id FROM book WHERE book_name = 'Hamlet')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Armin van'),
        (SELECT book_id FROM book WHERE book_name = 'Madame Bovary')
    );



