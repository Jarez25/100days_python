CREATE DATABASE ANIMALES; -- crea la base de datos
show databases; -- muestra la base de datos
use ANIMALES; -- selecion la base de datos de uso

CREATE TABLE CARNIVOROS( -- crea la tabla
id int,
estado varchar(30),
zona varchar(30),
primary key (id)
);

INSERT INTO CARNIVOROS (id, estado, zona) -- isnerta los datos de la tabla
VALUES (1, 'salvaje', 'selva'),
       (2, 'en cautiverio', 'sabana'),
       (3, 'en cautiverio', 'bosque'),
       (4, 'salvaje', 'desierto');

SELECT * FROM carnivoros;
SELECT * FROM carnivoros WHERE ID = 1;
SELECT * FROM carnivoros WHERE ESTADO = 'salvaje';
SELECT * FROM carnivoros WHERE ESTADO = 'salvaje' AND ID = 1;
DELETE * FROM ANIMALES WHERE ID = 3;

ALTER TABLE animales MODIFY COLUMN ID INT AUTO_INCREMENT -- cambia la los valore  de id para que se auto incrementen