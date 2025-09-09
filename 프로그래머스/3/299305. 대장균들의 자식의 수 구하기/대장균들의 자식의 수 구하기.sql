select id, ifnull((select count(id) from ecoli_data as b 
            where a.id = b.parent_id group by b.parent_id),0) as child_count
from ecoli_data as a
order by 1 