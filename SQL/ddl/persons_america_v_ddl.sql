DROP VIEW persons_america_v;
CREATE
VIEW `persons_america_v` AS
    SELECT 
        `persons`.`person_id` AS `person_id`,
        `persons`.`first_name` AS `first_name`,
        `persons`.`last_name` AS `last_name`,
        `persons`.`birthday` AS `birthday`,
        `persons`.`country` AS `country`,
        TIMESTAMPDIFF(YEAR,birthday,CURDATE()) AS age
    FROM
        `persons`
    WHERE
        (`persons`.`country` = 'United States of America')