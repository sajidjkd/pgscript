CREATE TABLE IF NOT EXISTS testschema.test(
    test_id                  INTEGER NOT NULL,
    test_cd                  CHARACTER VARYING(200) NOT NULL
)
WITH (
OIDS=FALSE
);
