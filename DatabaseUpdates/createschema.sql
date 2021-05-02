CREATE TABLE pack (
   packid SERIAL PRIMARY KEY,
   solutions INTEGER NOT NULL,
   packprice INTEGER NOT NULL
);

CREATE TABLE chat (
   chatid SERIAL PRIMARY KEY,
   packid INTEGER,
   telegramid INTEGER NOT NULL,
   packpurchasedate TIMESTAMP,
   availedsolutions INTEGER DEFAULT 0,
   FOREIGN KEY(packid) REFERENCES pack (packid)
);

