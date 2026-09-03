CREATE DATABASE AdoptaAPI;
GO
USE AdoptaAPI;
GO

-- Tabla USUARIO
CREATE TABLE USUARIO (
    Id_Usuario  INT PRIMARY KEY IDENTITY(1,1),
    Nombre      NVARCHAR(150) NOT NULL,
    Email       NVARCHAR(255) NOT NULL UNIQUE,
    Telefono    NVARCHAR(20),
    Ciudad      NVARCHAR(100) NOT NULL
);

-- Tabla FUNDACION
CREATE TABLE FUNDACION (
    Id_Fundacion INT PRIMARY KEY IDENTITY(1,1),
    Id_Usuario   INT NOT NULL UNIQUE,
    Nombre       NVARCHAR(200) NOT NULL,
    Descripcion  NVARCHAR(MAX),
    FOREIGN KEY (Id_Usuario) REFERENCES USUARIO(Id_Usuario)
);

-- Tabla MASCOTA
CREATE TABLE MASCOTA (
    Id_Mascota    INT PRIMARY KEY IDENTITY(1,1),
    Id_Fundacion  INT NOT NULL,
    Nombre        NVARCHAR(150) NOT NULL,
    Especie       NVARCHAR(50)  NOT NULL,
    Edad          INT NOT NULL,
    Tamano        NVARCHAR(20)  NOT NULL,
    Ciudad        NVARCHAR(100) NOT NULL,
    Descripcion   NVARCHAR(MAX),
    Estado        NVARCHAR(20)  NOT NULL,
    FechaRegistro DATETIME2 NOT NULL DEFAULT SYSUTCDATETIME(),
    FOREIGN KEY (Id_Fundacion) REFERENCES FUNDACION(Id_Fundacion),
    CONSTRAINT CK_MASCOTA_Edad   CHECK (Edad >= 0 AND Edad <= 50),
    CONSTRAINT CK_MASCOTA_Estado CHECK (Estado IN ('Disponible','EnProceso','Adoptada','Retirada')),
    CONSTRAINT CK_MASCOTA_Tamano CHECK (Tamano IN ('Pequeno','Mediano','Grande'))
);

-- Tabla SOLICITUD_ADOPCION
CREATE TABLE SOLICITUD_ADOPCION (
    Id_Solicitud   INT PRIMARY KEY IDENTITY(1,1),
    Id_Mascota     INT NOT NULL,
    Id_Usuario     INT NOT NULL,
    Estado         NVARCHAR(20) NOT NULL,
    Mensaje        NVARCHAR(MAX),
    FechaSolicitud DATETIME2 NOT NULL DEFAULT SYSUTCDATETIME(),
    FOREIGN KEY (Id_Mascota) REFERENCES MASCOTA(Id_Mascota),
    FOREIGN KEY (Id_Usuario) REFERENCES USUARIO(Id_Usuario),
    CONSTRAINT CK_SOLICITUD_Estado CHECK (Estado IN ('Pendiente','EnRevision','Aprobada','Rechazada','Completada'))
);
GO

-- Datos de prueba

INSERT INTO USUARIO (Nombre, Email, Telefono, Ciudad) VALUES
 ('Patricia Velez',    'patricia@adoptame.org',     '3105551001', 'Bogota'),
 ('Carlos Mendez',     'carlos@hogarfeliz.org',     '3105551002', 'Medellin'),
 ('Lucia Fernandez',   'lucia@rescatcanino.org',   '3105551003', 'Cali'),
 ('Jorge Herrera',     'jorge@patitas.org',         '3105551004', 'Barranquilla'),
 ('Mariana Ruiz',      'mariana@amigosfelinos.org', '3105551005', 'Cartagena'),
 ('Andres Torres',     'andres@refugioanimal.org', '3105551006', 'Bucaramanga'),
 ('Camila Diaz',       'camila@huellitas.org',      '3105551007', 'Pereira'),
 ('Santiago Gomez',    'santiago@salvavidas.org',   '3105551008', 'Manizales'),
 ('Valentina Castro',  'valentina@animalia.org',    '3105551009', 'Ibague'),
 ('Diego Romero',      'diego@compasion.org',       '3105551010', 'Santa Marta');
GO

INSERT INTO FUNDACION (Id_Usuario, Nombre, Descripcion) VALUES
 (1,  'Adoptame Bogota',           'Rescate de perros y gatos en Bogota'),
 (2,  'Hogar Feliz Medellin',      'Refugio con programa de padrinazgo'),
 (3,  'Rescate Canino Cali',       'Especializados en perros de calle'),
 (4,  'Patitas Barranquilla',      'Refugio costero de mascotas'),
 (5,  'Amigos Felinos',           'Hogar dedicado a gatos rescatados'),
 (6,  'Refugio Animal Bucaramanga','Rescate y adopcion responsable'),
 (7,  'Huellitas Pereira',         'Pequeno refugio familiar'),
 (8,  'Salvavidas Manizales',      'Rescate de mascotas en Caldas'),
 (9,  'Animalia Ibague',           'Fundacion de proteccion animal'),
 (10, 'Compasion Santa Marta',     'Refugio en la costa caribe');
GO

INSERT INTO MASCOTA (Id_Fundacion, Nombre, Especie, Edad, Tamano, Ciudad, Descripcion, Estado) VALUES
 (1, 'Luna',   'Perro', 2, 'Mediano', 'Bogota',       'Juguetona, vacunada',                    'EnProceso'),
 (1, 'Michi',  'Gato',  1, 'Pequeno', 'Bogota',       'Tranquila, ideal para apartamento',      'Adoptada'),
 (2, 'Rocky',  'Perro', 4, 'Grande',  'Medellin',    'Obediente, bueno con ninos',             'EnProceso'),
 (2, 'Nina',   'Gato',  3, 'Mediano', 'Medellin',    'Cariñosa, esterilizada',                 'Adoptada'),
 (3, 'Toby',   'Perro', 1, 'Pequeno', 'Cali',         'Cachorro activo',                        'EnProceso'),
 (3, 'Pelusa', 'Gato',  5, 'Mediano', 'Cali',         'Adulto tranquilo',                       'Disponible'),
 (4, 'Bruno',  'Perro', 2, 'Grande',  'Barranquilla', 'Leal y protector',                      'EnProceso'),
 (5, 'Mia',    'Gato',  2, 'Pequeno', 'Cartagena',   'Sociable con otras mascotas',            'EnProceso'),
 (6, 'Max',    'Perro', 3, 'Mediano', 'Bucaramanga', 'Energetico, necesita espacio',           'EnProceso'),
 (7, 'Bella',  'Gato',  4, 'Pequeno', 'Pereira',     'Timida al principio, cariñosa despues',  'Adoptada');
GO

INSERT INTO SOLICITUD_ADOPCION (Id_Mascota, Id_Usuario, Estado, Mensaje) VALUES
 (1, 5,  'Pendiente',   'Me encantaria adoptar a Luna, tengo patio amplio'),
 (2, 5,  'Aprobada',    'Michi sera perfecta para mi apartamento'),
 (3, 6,  'EnRevision',  'Interesado en Rocky, espero respuesta'),
 (4, 6,  'Completada', 'Ya tengo a Nina en casa, gracias'),
 (5, 7,  'Pendiente',   'Toby es adorable, quiero llevarlo a Pereira'),
 (6, 7,  'Rechazada',   'No pude viajar por la adopcion'),
 (7, 8,  'Pendiente',   'Bruno me parece perfecto para mi familia'),
 (8, 8,  'EnRevision',  'Mia parece ideal, tengo otra gata'),
 (9, 9,  'Pendiente',   'Max necesita espacio y yo tengo finca'),
 (10,10,'Completada',  'Bella ya esta en su nuevo hogar');
GO
