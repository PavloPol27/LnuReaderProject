CREATE DATABASE BookProject;

CREATE DOMAIN not_negative_page as int
	CHECK (value > 0);

DROP TABLE IF EXISTS Book CASCADE;
CREATE TABLE Book(
	file_path text PRIMARY KEY,
	file_name text,
	author varchar(20),
	genre varchar(20),
	published Date,
	file_stoped_page not_negative_page
);

DROP TABLE IF EXISTS Note CASCADE;
CREATE TABLE Note(
	note_id serial PRIMARY KEY,
	note_text text,
	note_page not_negative_page,
	note_line int,
	note_in_book text REFERENCES Book
);

DROP TABLE IF EXISTS Quotation CASCADE;
CREATE TABLE Quotation(
	quote_id serial PRIMARY KEY,
	quote_text text,
	quote_page not_negative_page,
	quote_line int,
	quote_in_book text REFERENCES Book
);

DROP TABLE IF EXISTS Bookmark CASCADE;
CREATE TABLE Bookmark(
	bookmark_id serial PRIMARY KEY,
	bookmark_page not_negative_page,
	bookmark_in_book text REFERENCES Book
);

DROP TABLE IF EXISTS library CASCADE; 
CREATE TABLE Library(
	library_id serial PRIMARY KEY,
	library_name varchar(50)
);

DROP TABLE IF EXISTS Books_and_libraries CASCADE; 
CREATE TABLE Books_and_libraries(
	link_id serial PRIMARY KEY,
	library_id int REFERENCES library,
	file_path text REFERENCES Book
);





