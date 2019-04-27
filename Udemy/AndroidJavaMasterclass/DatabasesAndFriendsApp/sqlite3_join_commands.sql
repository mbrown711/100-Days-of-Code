.schema;

.headers on;

SELECT name FROM albums WHERE _id = 367;

SELECT * FROM albums WHERE _id = 367;

INSERT INTO artists VALUES(201, "OAR");

SELECT * FROM albums ORDER BY name COLLATE NOCASE;

SELECT * FROM albums ORDER BY name DESC;

SELECT * FROM albums ORDER BY artist, name COLLATE NOCASE;

SELECT * FROM albums WHERE _id = 133;

SELECT * FROM artists WHERE _id = 133;

SELECT songs.track, songs.title, albums.name FROM songs JOIN albums ON songs.album = albums._id;

