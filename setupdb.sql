-- configuration database for AirBnB project

-- creates database reservasapp
CREATE DATABASE IF NOT EXISTS reservasapp;

-- creates a database user hbnb_dev
CREATE USER IF NOT EXISTS 'reservasapp_dev'@'localhost' identified by --aka su password--;

-- add privileges to the user reservasapp_dev
GRANT ALL PRIVILEGES ON reservasapp.* TO 'reservasapp_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'reservasapp_dev'@'localhost';




-- insert registers in doc_type table
INSERT INTO `api_doctype` (`code`, `short`, `name`) VALUES ('C', 'CC.', 'Cedula De Ciudadania');
INSERT INTO `api_doctype` (`code`, `short`, `name`) VALUES ('N', 'NIT', 'NIT');
INSERT INTO `api_doctype` (`code`, `short`, `name`) VALUES ('P', 'PA.', 'Pasaporte');
INSERT INTO `api_doctype` (`code`, `short`, `name`) VALUES ('E', 'CE.', 'Cédula De Extrangería');
INSERT INTO `api_doctype` (`code`, `short`, `name`) VALUES ('T', 'TI.', 'Tarjeta de Identidad');
INSERT INTO `api_doctype` (`code`, `short`, `name`) VALUES ('U', 'RC.', 'Registro Civil');
INSERT INTO `api_doctype` (`code`, `short`, `name`) VALUES ('D', 'CD.', 'Carnet Diplomático');
