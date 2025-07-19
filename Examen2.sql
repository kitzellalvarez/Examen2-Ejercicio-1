CREATE DATABASE Examen2
go

use Examen2 
go

CREATE TABLE palabras (
    id INT PRIMARY KEY,
    texto VARCHAR(255),
    grupo_id INT
);
go

INSERT INTO palabras (id, texto, grupo_id) VALUES
(1,  'perro', 1),
(2,  '   Gato', 1),
(3,  'SOL', 1),
(4,  'agua clara', 1),
(5,  '  cielo azul  ', 1),
(6,  'tigre', 1),
(7,  'Elefante', 1),
(8,  'ratón', 1),
(9,  'león', 1),
(10, 'jirafa', 1),
(11, 'computadora', 2),
(12, 'Python 3.10', 2),
(13, 'clase de programación', 2),
(14, '   código limpio   ', 2),
(15, 'variable', 2),
(16, '123', 2),
(17, 'Suma', 2),
(18, '123abc', 2),
(19, 'if else', 2),
(20, 'Función split()', 2),
(21, 'El árbol', 3),
(22, 'espacio exterior', 3),
(23, 'Marte', 3),
(24, 'Universo', 3),
(25, 'planeta Tierra', 3),
(26, 'satélite natural', 3),
(27, '123sol', 3),
(28, 'luz solar', 3),
(29, 'Nube', 3),
(30, 'atmósfera', 3),
(31, 'Python', 4),
(32, 'PYTHON', 4),
(33, 'python', 4),
(34, '  Python  ', 4),
(35, 'pyThOn', 4),
(36, 'PYthon', 4),
(37, 'pytHon', 4),
(38, 'python3', 4),
(39, 'PYTHONISTA', 4),
(40, 'programador python', 4),
(41, 'Camino', 5),
(42, 'caminar', 5),
(43, 'corriendo', 5),
(44, 'Corre', 5),
(45, 'jugar fútbol', 5),
(46, '123 calle', 5),
(47, ' final', 5),
(48, 'Centro', 5),
(49, 'norte', 5),
(50, 'sur', 5);

go