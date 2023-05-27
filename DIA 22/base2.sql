create database user;

use user; -- usa la base de datos

create table usuario( --  crea la tabla 
id int not null auto_increment,
name varchar (50) not null,
edad int not null,
email varchar (100) not null,
primary key(id)
);

insert into usuario (name, edad, email) values ('marcos', 18, 'jairo@gmail.com'); -- crea los campos en la tabla ingresando los valores de la tabla
insert into usuario (name, edad, email) values ('roberto', 16, 'jarez@gmail.com');-- seguido de el valor de estos valores
insert into usuario (name, edad, email) values ('Elias', 35, 'amanda@gmail.com');

select * from usuario;
select * from usuario where edad = 18; -- el where es como un condicional de busqueda en este caso de la tabla usuarios donde la edad sea = a 18 lo regresa
select * from usuario where edad >= 18; --  lo mismo que el de arriba solo que este muestra de 18 a mas
select * from usuario where edad = 35 or email = 'amanda@gmail.com'; -- mustra los valores donde edad sea 35 o coreo amanda@gmail.com
select * from usuario where edad = 35 and email = 'amanda@gmail.com'; -- muestra solo el valor si edad es 35 y el correo es amanda@gmail.com
select * from usuario where edad between 25 and 40; -- me railiza la consulta entre los campos en este caso seria entre 25 a 40
select * from usuario where email like '%jarez%';
select * from usuario where email like '%jarez'; -- es la palabra termiuna con la letras del final del %
select * from usuario where email like 'jarez%'; -- que la palabre inicie con la letra antes del %
select * from usuario order by edad asc; -- ordena los campos de forma acendente ya sea por numero o por letra
select * from usuario order by edad desc; -- ordenas los campos de forma desendemte ya sea numero o letra

select max(edad) as mayor from usuario; -- seleciona el valor maximo de edad y el as es para darle un alias
select min(edad) as mayor from usuario; -- seleciona el valor minimo de edad 

select id as numeroid, name as nombre from usuario; -- solo seleciona las columnas

