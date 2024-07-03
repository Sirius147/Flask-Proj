drop database restaurant;

drop table restaurant;
drop table menu_item;

CREATE DATABASE restaurant default CHARACTER SET UTF8;
-- db 생성

use restaurant;

use madang;
select * from customer;
select * from book where publisher='이상미디어' and price>=13000;

select * from restaurant;
select * from menu_item;

CREATE DATABASE bookstore default CHARACTER SET UTF8;
-- db 생성

use bookstore;