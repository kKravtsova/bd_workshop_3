CREATE OR REPLACE VIEW insurance_info  AS
SELECT
    human_insurance.human_id,
    human_trip.country_name,
	human_insurance.dis_channel,
    human_insurance.commision
FROM
         human_insurance
    INNER JOIN human_trip ON human_insurance.human_id = human_trip.human_id;