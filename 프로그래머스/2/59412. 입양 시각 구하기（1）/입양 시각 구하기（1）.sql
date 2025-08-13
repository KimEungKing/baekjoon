select hour(datetime) as hour, count(*)
from animal_outs
where time(datetime) between '09:00' and '19:59'
group by hour(datetime)
order by 1