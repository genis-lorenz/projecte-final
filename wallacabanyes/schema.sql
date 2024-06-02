DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS ad;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  grade TEXT NOT NULL
);

CREATE TABLE ad (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    contact TEXT,
    name TEXT NOT NULL,
    description TEXT,
    subjects TEXT NOT NULL,
    size TEXT,
    price REAL NOT NULL,
    FOREIGN KEY(user_id) REFERENCES user(id) ON DELETE CASCADE
);

CREATE TABLE img (
  ad_id INTEGER NOT NULL,
  filename TEXT NOT NULL,
  FOREIGN KEY(ad_id) REFERENCES ad(id) ON DELETE CASCADE
);

INSERT INTO user (username, password, grade)
VALUES ('test@alumnat.institutcabanyes.cat', 'test', 'CFGM');

INSERT INTO user (username, password, grade)
VALUES ('test2@alumnat.institutcabanyes.cat', 'test2', 'CFGS');

INSERT INTO ad (user_id, name, description, subjects, size, price)
SELECT user.id, 'Trek Caliber MTB', 'La bici solo tiene 200km','Bicicleta, Muntanya','M', 1099
FROM user
WHERE username = 'test@alumnat.institutcabanyes.cat';

INSERT INTO ad (user_id, name, description, subjects, size, price)
SELECT user.id, 'Aletes', 'Utilitzades una sola vegada','Lleure, Natació','L', 10
FROM user
WHERE username = 'test@alumnat.institutcabanyes.cat';

INSERT INTO img (ad_id, filename)
SELECT ad.id, '1-mtb.jpg'
FROM ad
WHERE name = 'Trek Caliber MTB'

INSERT INTO img (ad_id, filename)
SELECT ad.id, '1-aletes.jpg'
FROM ad
WHERE name = 'Aletes'

INSERT INTO ad (user_id, name, description, subjects, size, price)
SELECT user.id, 'Guants de boxe', 'Vermells','Lleure','12oz', 25
FROM user
WHERE username = 'test2@alumnat.institutcabanyes.cat';

INSERT INTO ad (user_id, name, description, subjects, size, price)
SELECT user.id, 'Mancuernas', 'De ferro','Dinàmica','10kg', 30
FROM user
WHERE username = 'test2@alumnat.institutcabanyes.cat';

INSERT INTO img (ad_id, filename)
SELECT ad.id, '1-boxe.jpg'
FROM ad
WHERE name = 'Guants de boxe'

INSERT INTO img (ad_id, filename)
SELECT ad.id, '1-mancuerna.jpg'
FROM ad
WHERE name = 'Mancuernas'