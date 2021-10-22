-- configuration database for Django rest api project

-- creates database reservasapp
CREATE DATABASE IF NOT EXISTS reservasapp;

-- creates a database user hbnb_dev
CREATE USER IF NOT EXISTS 'reservasapp_dev'@'localhost' identified by --aka su password--;

-- add privileges to the user reservasapp_dev
GRANT ALL PRIVILEGES ON reservasapp.* TO 'reservasapp_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'reservasapp_dev'@'localhost';
