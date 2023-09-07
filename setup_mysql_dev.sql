-- Database setup file for MySQL

CREATE DATABASE IF NOT EXISTS `Query-IP` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
CREATE USER IF NOT EXISTS 'dgregs'@'localhost' IDENTIFIED BY 'dgregs87';
GRANT ALL PRIVILEGES ON `Query-IP`.* TO 'dgregs'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'dgregs'@'localhost';
FLUSH PRIVILEGES;
