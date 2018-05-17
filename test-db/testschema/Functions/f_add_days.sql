CREATE OR REPLACE FUNCTION testschema.f_add_days
(
    IN datetochange INTEGER,
    IN daycount     INTEGER
)
RETURNS INTEGER
AS
$BODY$
BEGIN

    RETURN testschema.to_test_date(vestek.to_oracle_date(datetochange) + dayCount);

END;
$BODY$
LANGUAGE  plpgsql;

ALTER FUNCTION  testschema.f_add_days(INTEGER, INTEGER)
OWNER TO testdb;