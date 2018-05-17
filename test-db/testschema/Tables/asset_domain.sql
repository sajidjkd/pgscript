CREATE TABLE IF NOT EXISTS testschema.asset_domain(
asset_domain_cd                 CHARACTER VARYING(2) NOT NULL,
name                            CHARACTER VARYING(160) NOT NULL,
description                     CHARACTER VARYING(2000)
)
WITH (
OIDS=FALSE
);