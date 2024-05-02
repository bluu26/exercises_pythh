zad1 = """
create database exercises_db;

# query robimy na naszej bazie
1.
CREATE TABLE Products
(
id SERIAL primary key,
name varchar(100), #string do 100 znakow
description text,
price float
)
2.
CREATE TABLE orders(
id serial primary key,
description text

)

3.

CREATE TABLE Clients
(
id SERIAL primary key,
name varchar(100),
surname varchar(100)

)

insert into movies (name, description, rating) values
('film1', 'fajny film', 5.0),
('film2', 'ciekawy film', 4.0),
('film3', 'super film', 6.0),
('film4', 'HIT', 6.9);

insert into tickets (quantity, price) values
(5, 15.5),
(30, 17.5),
(120, 19.5),
(125, 32.0);

select * from movies where name LIKE 'f%';

select * from tickets where quantity > 3;

create table opinions (
id serial primary key,
description text,
product_id int,
foreign key(product_id) references products(id) # stworz pole na bazie id products
)


"""