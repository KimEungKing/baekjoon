select id, 
    case ntile(4) over(order by size_of_colony)
        when 4 then 'CRITICAL'
        when 3 then 'HIGH'
        when 2 then 'MEDIUM'
        when 1 then 'LOW'
    end as colony_name
from ecoli_data
order by 1