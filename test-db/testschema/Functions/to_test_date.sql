CREATE OR REPLACE FUNCTION testschema.to_test_date
(
    IN datetochange DATE
)
RETURNS INTEGER
AS
$BODY$
BEGIN
    RETURN TO_CHAR(datetochange, 'YYYYMMDD')::INTEGER;
END;
$BODY$
LANGUAGE  plpgsql
COST 100;

ALTER FUNCTION  testschema.to_test_date(DATE)
OWNER TO testdb;