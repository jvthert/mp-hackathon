DROP DATABASE IF EXISTS abc;

CREATE DATABASE abc;

ALTER DATABASE abc CHARACTER SET utf8 COLLATE utf8_unicode_ci;

USE abc;

CREATE TABLE user (
        id int(11) NOT NULL AUTO_INCREMENT,
        name  varchar(255),
        PRIMARY KEY(id)
) ENGINE InnoDB DEFAULT CHARSET=utf8; 

CREATE TABLE item (
        id int(11) NOT NULL AUTO_INCREMENT,
        title  varchar(255),
        photo varchar(255),
        description varchar(255),
        PRIMARY KEY(id)
) ENGINE InnoDB DEFAULT CHARSET=utf8; 


CREATE TABLE appraisal (
	item_id int(11) NOT NULL,
	user_id int(11) NOT NULL,
	price int(11) NOT NULL DEFAULT '0'
) ENGINE InnoDB DEFAULT CHARSET=utf8;

INSERT INTO item (id, title, photo, description) VALUES (1, 'iphone5', 'http://i.marktplaats.com/00/s/MzAwWDIwOQ==/$T2eC16N,!)EE9s2ufhNfBROt4hL7YQ~~60_84.JPG', '');
INSERT INTO item (id, title, photo, description) VALUES (2, 'samsung galaxy s5', 'http://i.marktplaats.com/00/s/Mjk0WDI5NA==/z/P10AAOSwstxVBww-/$_84.JPG', '');
INSERT INTO item (id, title, photo, description) VALUES (3, 'Nieuwe Transportfietsen bij Prijskiller.nl', 'http://i.marktplaats.com/00/s/NjUwWDY1MA==/z/X-AAAOSw8d9Uxj22/$_84.JPG', 'Mooie Transportfietsen (met en zonder versnellingen)');
INSERT INTO item (id, title, photo, description) VALUES (4, 'antiek rond tafel', 'http://i.marktplaats.com/00/s/NzI2WDU0NQ==/z/GXwAAOSwBahVSy9t/$_84.JPG', 'Doorsnee 27,5 cm en 54 cm hoog. Het bovenblad kan rondgedraaid worden');
INSERT INTO item (id, title, photo, description) VALUES (5, 'Abstract schilderij', 'http://i.marktplaats.com/00/s/NjAwWDgwMA==/z/I-oAAOSwEeFVSxzI/$_84.JPG', '60x80 cm');


