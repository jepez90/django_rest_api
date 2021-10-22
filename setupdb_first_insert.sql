-- execute this script after the first migrate in django

-- insert registers in doc_type table
INSERT INTO `api_doctype` (`code`, `short`, `name`) VALUES ('C', 'CC.', 'Cedula De Ciudadania');
INSERT INTO `api_doctype` (`code`, `short`, `name`) VALUES ('N', 'NIT', 'NIT');
INSERT INTO `api_doctype` (`code`, `short`, `name`) VALUES ('P', 'PA.', 'Pasaporte');
INSERT INTO `api_doctype` (`code`, `short`, `name`) VALUES ('E', 'CE.', 'Cédula De Extrangería');
INSERT INTO `api_doctype` (`code`, `short`, `name`) VALUES ('T', 'TI.', 'Tarjeta de Identidad');
INSERT INTO `api_doctype` (`code`, `short`, `name`) VALUES ('U', 'RC.', 'Registro Civil');
INSERT INTO `api_doctype` (`code`, `short`, `name`) VALUES ('D', 'CD.', 'Carnet Diplomático');


INSERT INTO `api_cartype` (`id`, `name`, `active`) VALUES (1, 'Livianos', b'1');
INSERT INTO `api_cartype` (`id`, `name`, `active`) VALUES (2, 'Motocicletas', b'1');
INSERT INTO `api_cartype` (`id`, `name`, `active`) VALUES (3, 'Pesados', b'0');
INSERT INTO `api_cartype` (`id`, `name`, `active`) VALUES (4, 'Motocarro', b'0');
INSERT INTO `api_cartype` (`id`, `name`, `active`) VALUES (5, 'Cuatrimoto', b'0');


INSERT INTO `api_revisiontype` (`id`, `name`) VALUES (1, 'Inspeccion');
INSERT INTO `api_revisiontype` (`id`, `name`) VALUES (2, 'Reinspeccion');
INSERT INTO `api_revisiontype` (`id`, `name`) VALUES (3, 'Preventiva');
