create database matricula_alumnos;

use matricula_alumnos;

-- Tabla carreras
create table carreras(
	carrera_id BIGINT PRIMARY KEY AUTO_INCREMENT,
	nombre VARCHAR(50) NOT NULL,
	numero_ciclos INT NOT NULL
);

-- Tabla alumnnos
create table alumnos(
	alumno_id BIGINT PRIMARY KEY AUTO_INCREMENT,
	nombre_completo VARCHAR(50) NOT NULL,
	dni VARCHAR(10) NOT NULL,
	telefono VARCHAR(15) NOT NULL,
	correo VARCHAR(50) NOT NULL,
	contrasenia VARCHAR(50) NOT NULL,
	codigo_alumno VARCHAR(8) NOT NULL,
	fecha_nacimiento DATE NOT NULL,
	direccion VARCHAR(50) NOT NULL,
	sexo VARCHAR(12) NOT NULL,
	carrera_id BIGINT NOT NULL,
	FOREIGN KEY (carrera_id) REFERENCES carreras(carrera_id)
);

-- Tabla matriculas
create table matriculas(
	matricula_id BIGINT PRIMARY KEY AUTO_INCREMENT,
	fecha_matricula DATE NOT NULL,
	alumno_id BIGINT NOT NULL,
	carrera_id BIGINT NOT NULL,
	FOREIGN KEY (alumno_id) REFERENCES alumnos(alumno_id),
	FOREIGN KEY (carrera_id) REFERENCES carreras(carrera_id)
);

-- Tabla cursos
create table cursos(
	cursos_id BIGINT PRIMARY KEY AUTO_INCREMENT,
	nombre VARCHAR(50) NOT NULL,
	horario TIME NOT NULL,
	cantidad_horas INT NOT NULL,
	numero_creditos INT NOT NULL,
	carrera_id BIGINT NOT NULL,
	FOREIGN KEY (carrera_id) REFERENCES carreras(carrera_id)
);

-- Tabla pagos
create table pagos(
	pagos_id BIGINT PRIMARY KEY AUTO_INCREMENT,
	monto INT NOT NULL,
	numero_cuota INT NOT NULL,
	fecha_pago DATE NOT NULL,
	estado_pago VARCHAR(50),
	matricula_id BIGINT NOT NULL,
	FOREIGN KEY (matricula_id) REFERENCES matriculas(matricula_id)
);

-- Insertar las tres carreras en la tabla 'carreras'
INSERT INTO carreras (nombre, numero_ciclos) VALUES ('Ingeniería', 10);
INSERT INTO carreras (nombre, numero_ciclos) VALUES ('Negocios', 8);
INSERT INTO carreras (nombre, numero_ciclos) VALUES ('Ciencias de la Salud', 9);

-- Cursos de ingenieria
INSERT INTO cursos (nombre, horario, cantidad_horas, numero_creditos, carrera_id) VALUES 
('Inteligencia Artificial y Machine Learning', '08:00:00', 40, 4, 1),
('Big Data y Análisis de Datos', '10:00:00', 35, 3, 1),
('Desarrollo de Software Avanzado', '12:00:00', 45, 5, 1),
('Ingeniería Robótica', '14:00:00', 50, 5, 1),
('Simulación y Modelado', '09:00:00', 30, 3, 1),
('Redes y Ciberseguridad', '11:00:00', 35, 3, 1),
('Ingeniería de Sistemas en la Nube', '13:00:00', 40, 4, 1),
('Sistemas Embebidos', '15:00:00', 45, 4, 1),
('Automatización y Control Industrial', '16:00:00', 30, 3, 1),
('Ingeniería de Software para IoT', '17:00:00', 40, 4, 1);

-- Cursos para negocios
INSERT INTO cursos (nombre, horario, cantidad_horas, numero_creditos, carrera_id) VALUES 
('Gestión de Proyectos y Metodologías Ágiles', '08:00:00', 30, 3, 2),
('Análisis Financiero', '09:00:00', 25, 2, 2),
('Data Analytics para Negocios', '10:00:00', 35, 3, 2),
('Marketing Digital y Estrategia de Marca', '11:00:00', 30, 3, 2),
('Liderazgo y Coaching Empresarial', '12:00:00', 20, 2, 2),
('Comercio Internacional', '13:00:00', 40, 4, 2),
('Emprendimiento e Innovación', '14:00:00', 35, 3, 2),
('Business Intelligence (BI)', '15:00:00', 30, 3, 2),
('Transformación Digital', '16:00:00', 40, 4, 2),
('Fintech y Tecnología Financiera', '17:00:00', 30, 3, 2);

-- Cursos de ciencias de la salud
INSERT INTO cursos (nombre, horario, cantidad_horas, numero_creditos, carrera_id) VALUES 
('Bioinformática', '08:00:00', 30, 3, 3),
('Telemedicina y Salud Digital', '09:00:00', 25, 2, 3),
('Farmacología y Terapias Avanzadas', '10:00:00', 35, 3, 3),
('Biotecnología Médica', '11:00:00', 30, 3, 3),
('Neurociencia', '12:00:00', 40, 4, 3),
('Epidemiología', '13:00:00', 35, 3, 3),
('Investigación Clínica', '14:00:00', 40, 4, 3),
('Psicología de la Salud', '15:00:00', 30, 3, 3),
('Salud Pública y Política Sanitaria', '16:00:00', 40, 4, 3),
('Nutrición y Dietética', '17:00:00', 30, 3, 3);