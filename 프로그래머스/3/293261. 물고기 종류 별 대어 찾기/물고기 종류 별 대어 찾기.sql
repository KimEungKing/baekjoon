select i.id, n.fish_name, i.length
from fish_info as i 
join fish_name_info as n on i.fish_type = n.fish_type
where i.length = (select max(length)
                 from fish_info as i2 
                 where i.fish_type = i2.fish_type)
order by 1