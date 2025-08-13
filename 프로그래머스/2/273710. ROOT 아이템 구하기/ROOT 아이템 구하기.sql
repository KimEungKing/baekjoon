SELECT u.item_id, u.item_name
from item_info as u
join item_tree as t on u.item_id = t.item_id 
where t.parent_item_id is null
order by 1 asc 