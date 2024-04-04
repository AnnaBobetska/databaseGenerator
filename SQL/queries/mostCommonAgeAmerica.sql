select max(age_count) as most_frequent_age
from (
	select age, count(*) as age_count
	from persons_america_v
	group by age
	) ilv