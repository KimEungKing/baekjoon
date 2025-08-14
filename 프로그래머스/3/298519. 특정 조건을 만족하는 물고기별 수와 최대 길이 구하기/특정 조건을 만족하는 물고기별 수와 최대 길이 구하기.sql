select count(id) as FISH_COUNT, max(length) as MAX_LENGTH, FISH_TYPE
from fish_info
group by fish_type
having avg(if(length>10, length, 10)) >= 33
order by 3 asc 
