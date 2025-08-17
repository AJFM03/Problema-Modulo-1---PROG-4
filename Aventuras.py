DROP TABLE IF EXISTS misiones_monstruos;
DROP TABLE IF EXISTS misiones_heroes;
DROP TABLE IF EXISTS monstruos;
DROP TABLE IF EXISTS misiones;
DROP TABLE IF EXISTS heroes;

-- Héroes
CREATE TABLE heroes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    clase TEXT NOT NULL CHECK(clase IN ('Guerrero','Mago','Arquero','Clérigo','Ladrón','Bárbaro','Paladín','Druida')),
    nivel_experiencia INTEGER NOT NULL CHECK(nivel_experiencia >= 1)
);

-- Misiones
CREATE TABLE misiones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    nivel_dificultad INTEGER NOT NULL CHECK(nivel_dificultad BETWEEN 1 AND 10),
    localizacion TEXT NOT NULL,
    recompensa INTEGER NOT NULL CHECK(recompensa >= 0)
);

-- Monstruos
CREATE TABLE monstruos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    tipo TEXT NOT NULL CHECK(tipo IN ('Dragón','Goblin','No-muerto','Orco','Bestia','Elemental','Demonio')),
    nivel_amenaza INTEGER NOT NULL CHECK(nivel_amenaza BETWEEN 1 AND 10)
);

-- Relación misiones - héroes
CREATE TABLE misiones_heroes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_mision INTEGER NOT NULL,
    id_heroe INTEGER NOT NULL,
    rol TEXT,
    FOREIGN KEY (id_mision) REFERENCES misiones(id) ON DELETE CASCADE,
    FOREIGN KEY (id_heroe) REFERENCES heroes(id) ON DELETE CASCADE,
    UNIQUE (id_mision, id_heroe)
);

-- Relación misiones - monstruos
CREATE TABLE misiones_monstruos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_mision INTEGER NOT NULL,
    id_monstruo INTEGER NOT NULL,
    cantidad INTEGER NOT NULL DEFAULT 1 CHECK(cantidad >= 1),
    FOREIGN KEY (id_mision) REFERENCES misiones(id) ON DELETE CASCADE,
    FOREIGN KEY (id_monstruo) REFERENCES monstruos(id) ON DELETE CASCADE,
    UNIQUE (id_mision, id_monstruo)
);

-- =========================
-- DATOS DE PRUEBA
-- =========================

-- Héroes
INSERT INTO heroes (nombre, clase, nivel_experiencia) VALUES
('Arthas', 'Paladín', 15),
('Jaina', 'Mago', 20),
('Legolas', 'Arquero', 18),
('Thrall', 'Guerrero', 22),
('Valeera', 'Ladrón', 12);

-- Misiones
INSERT INTO misiones (nombre, nivel_dificultad, localizacion, recompensa) VALUES
('Defensa del Pueblo', 3, 'Villa del Río', 150),
('Asalto a la Cueva del Dragón', 9, 'Montaña Escarlata', 1200),
('Patrulla contra No-muertos', 5, 'Cementerio Antiguo', 400),
('Caza de Orcos', 6, 'Bosque Sombrío', 600);

-- Monstruos
INSERT INTO monstruos (nombre, tipo, nivel_amenaza) VALUES
('Ragnaros', 'Elemental', 10),
('Onyxia', 'Dragón', 9),
('Goblin Asaltante', 'Goblin', 3),
('Orco Berserker', 'Orco', 6),
('Liche Ancestral', 'No-muerto', 8);

-- Relación Misiones - Héroes
INSERT INTO misiones_heroes (id_mision, id_heroe, rol) VALUES
(1, 1, 'Líder'),
(1, 3, 'Soporte'),
(2, 2, 'Líder'),
(2, 4, 'Tanque'),
(3, 2, 'Hechicera'),
(3, 5, 'Exploradora'),
(4, 3, 'Arquero'),
(4, 5, 'Asesina');

-- Relación Misiones - Monstruos
INSERT INTO misiones_monstruos (id_mision, id_monstruo, cantidad) VALUES
(1, 3, 5), -- Goblins en defensa del pueblo
(2, 2, 1), -- Dragón Onyxia
(2, 1, 1), -- Ragnaros elemental
(3, 5, 2), -- Liches
(4, 4, 7); -- Orcos Berserker
