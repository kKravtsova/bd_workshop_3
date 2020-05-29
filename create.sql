CREATE TABLE country (
    country_name VARCHAR2(50) NOT NULL
);

ALTER TABLE country ADD CONSTRAINT country_pk PRIMARY KEY ( country_name );

CREATE TABLE human (
    human_id       INTEGER NOT NULL,
    human_gender   VARCHAR2(6)
);

ALTER TABLE human ADD CONSTRAINT human_pk PRIMARY KEY ( human_id );

CREATE TABLE human_insurance (
    human_id           INTEGER NOT NULL,
    insurance_agency   VARCHAR2(50) NOT NULL,
    insurance_name     VARCHAR2(50) NOT NULL,
	commision         FLOAT NOT NULL,
	dis_channel			VARCHAR2(8) NOT NULL
	
);

ALTER TABLE human_insurance
    ADD CHECK ( dis_channel IN (
        'offline',
        'online'
    ) );

ALTER TABLE human_insurance
    ADD CONSTRAINT human_incurance_pk PRIMARY KEY ( human_id,
                                                    insurance_agency,
                                                    insurance_name );
													
CREATE TABLE human_trip (
    human_id       INTEGER NOT NULL,
    country_name   VARCHAR2(50) NOT NULL,
	duration       INTEGER NOT NULL
);

ALTER TABLE human_trip ADD CONSTRAINT human_trip_pk PRIMARY KEY ( human_id );

CREATE TABLE insurance (
    insurance_agency   VARCHAR2(50) NOT NULL,
    insurance_type     VARCHAR2(50) NOT NULL
);

ALTER TABLE insurance ADD CONSTRAINT insurance_pk PRIMARY KEY ( insurance_agency,
                                                                insurance_type );

ALTER TABLE human_insurance
    ADD CONSTRAINT human_incurance_human_fk FOREIGN KEY ( human_id )
        REFERENCES human ( human_id );

ALTER TABLE human_insurance
    ADD CONSTRAINT human_incurance_insurance_fk FOREIGN KEY ( insurance_agency,
                                                              insurance_type )
        REFERENCES insurance ( insurance_agency,
                               insurance_type );

ALTER TABLE human_trip
    ADD CONSTRAINT human_trip_country_fk FOREIGN KEY ( country_name )
        REFERENCES country ( country_name );

ALTER TABLE human_trip
    ADD CONSTRAINT human_trip_human_fk FOREIGN KEY ( human_id )
        REFERENCES human ( human_id );