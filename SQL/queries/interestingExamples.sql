select first_name, count(*)
from persons_america_v
group by first_name
having count(*) = 1

select first_name , row_number() over (order by person_ID) row_num
from persons_america_v
where first_name = 'Franklin'