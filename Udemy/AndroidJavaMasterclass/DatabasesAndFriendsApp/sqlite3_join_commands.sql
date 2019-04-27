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

SELECT track, title, name FROM sings JOIN albums ON songs.album = alnums._id;

SELECT songs.track, songs.title, albums.name FROM songs INNER JOIN albums ON songs.album = albums._id;

SELECT albums.name, songs.track, songs.title FROM songs INNER JOIN albums ON songs.album = albums._id ORDER BY albums.name, songs.track; 

-- make a list of all artists with their albums in alphabetical order of artist name:

SELECT artists.name, albums.name FROM albums INNER JOIN artists ON albums.artist = artists._id ORDER BY artists.name;

-- chaining join statements together:

SELECT artists.name, albums.name, songs.track, songs.title FROM songs INNER JOIN albums ON songs.album = albums._id INNER JOIN artists ON albums.artist = artists._id ORDER BY artists.name, albums.name, songs.track;

-- show titles of all songs on the album titled "Forbidden":

SELECT songs.title FROM songs INNER JOIN albums ON songs.album = albums._id WHERE albums.name = "Forbidden";

-- show songs from above in track order, include track number to verify

SELECT songs.track, songs.title FROM songs INNER JOIN albums ON songs.album = albums._id WHERE albums.name = "Forbidden" ORDER BY songs.track;

-- Display all songs by the band "Deep Purple"

SELECT songs.title FROM songs INNER JOIN albums ON songs.album = albums._id INNER JOIN artists ON albums.artist = artists._id WHERE artists.name = "Deep Purple";

-- Rename the band Billy Joel to "one kitten"

UPDATE artists SET name = "One Kitten" WHERE artists.name = "Billy Joel";

SELECT * FROM artists WHERE name = "One Kitten";