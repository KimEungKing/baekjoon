select i.animal_id, i.name 
from animal_ins as i 
left join animal_outs as o on i.animal_id = o.animal_id
where o.datetime is not null
order by timestampdiff(second, i.datetime, o.datetime) desc
limit 2 