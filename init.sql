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

INSERT INTO item (id, title, photo, description) VALUES (4, 'antiek rond tafel', 'http://i.marktplaats.com/00/s/NzI2WDU0NQ==/z/GXwAAOSwBahVSy9t/$_84.JPG', 'Doorsnee 27,5 cm en 54 cm hoog. Het bovenblad kan rondgedraaid worden');
INSERT INTO item (id, title, photo, description) VALUES (5, 'Abstract schilderij', 'http://i.marktplaats.com/00/s/NjAwWDgwMA==/z/I-oAAOSwEeFVSxzI/$_84.JPG', '60x80 cm');
INSERT INTO item (id, title, photo, description) VALUES (6, '6-persoons Zilver Bestek', 'http://i.marktplaats.com/00/s/OTk1WDEwMjQ=/z/61gAAOSwrklVSzRw/$_84.JPG', '890 gram, gemerkt met BSF.');
INSERT INTO item (id, title, photo, description) VALUES (7, 'Racing bike', '/img/bike1.jpeg', 'Looks cool, rides smooth');
INSERT INTO item (id, title, photo, description) VALUES (8, 'Ray Ban zonnebril', 'http://i.marktplaats.com/00/s/NTAwWDY2Nw==/z/WWAAAOSwEeFVS2TM/$_85.JPG', 'wayfare');
INSERT INTO item (id, title, photo, description) VALUES (9, 'Stoffen 2 zitter bank', 'http://i.marktplaats.com/00/s/NTQ1WDcyNg==/z/ZP4AAOSwNSxVS3lc/$_84.JPG', '1,50 breed, 65 hoog, 85 diep');
INSERT INTO item (id, title, photo, description) VALUES (10, 'Witte retro vloerlamp', '/img/lamp1.jpg', '1.5m hoog, verstelbaar');
INSERT INTO item (id, title, photo, description) VALUES (11, 'Gazelle Madeo fiets', 'http://i.marktplaats.com/00/s/NDUwWDgwMA==/z/S0YAAOSwstxVQks4/$_85.JPG', '54cm frame, 24 gears, with lock');
INSERT INTO item (id, title, photo, description) VALUES (12, 'Babboe Big Bakfiets', 'http://i.marktplaats.com/00/s/NzY4WDEwMjQ=/z/I84AAOSwPhdVLpGn/$_85.JPG', '5 gears, for 4 kids');