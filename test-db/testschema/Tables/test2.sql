
CREATE TABLE IF NOT EXISTS testschema.test2(
    test_id                  INTEGER NOT NULL,
    test_cd                  CHARACTER VARYING(200) NOT NULL,
    test_cd1                 CHARACTER VARYING(200) NOT NULL
)
WITH (
OIDS=FALSE
);
