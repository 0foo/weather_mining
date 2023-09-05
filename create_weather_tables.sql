DROP TABLE monthly; 

CREATE TABLE monthly (
    key TEXT NOT NULL UNIQUE,
    station TEXT NOT NULL,
    month TEXT NOT NULL,
    element TEXT NOT NULL,
    average REAL NOT NULL,
    stdev REAL NOT NULL,
    max REAL NOT NULL,
    min REAL NOT NULL,
    valuecount INTEGER NOT NULL
);


