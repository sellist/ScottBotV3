BEGIN TRANSACTION;

DROP TABLE IF EXISTS name;

CREATE TABLE names (
	name_id serial,
	name varchar(50) NOT NULL,

	CONSTRAINT pk_name PRIMARY KEY (name)
);

COMMIT;