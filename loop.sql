DECLARE
   type agency_name_arr IS VARRAY(4) OF VARCHAR2(10);
   type agency_type_arr IS VARRAY(4) OF VARCHAR2(20);   
agency_name agency_name_arr;
agency_type agency_type_arr;

BEGIN
agency_name := agency_name_arr('CBH','CWT','JZI' ,'KML');
agency_type := agency_type_arr('Travel Agency','Travel Agency','Airlines','Travel Agency');

    FOR i IN 1 .. 4 
    LOOP
        INSERT INTO insurance_agency (agency_name, agency_type) VALUES (agency_name(i), agency_type(i));
        COMMIT;
    END LOOP;
	
END;
