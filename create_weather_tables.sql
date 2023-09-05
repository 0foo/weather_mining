DROP TABLE monthly; 
DROP TABLE stations;

CREATE TABLE monthly (
    key TEXT NOT NULL UNIQUE,
    stationmonth TEXT NOT NULL,
    station TEXT NOT NULL,
    month TEXT NOT NULL,
    element TEXT NOT NULL,
    average REAL NOT NULL,
    stdev REAL NOT NULL,
    max REAL NOT NULL,
    min REAL NOT NULL,
    valuecount INTEGER NOT NULL
);


CREATE TABLE stations (
    stationid TEXT NOT NULL UNIQUE,
    lat REAL NOT NULL,
    long REAL NOT NULL,
    elevation REAL NOT NULL,
    state TEXT NOT NULL,
    name TEXT NOT NULL
);