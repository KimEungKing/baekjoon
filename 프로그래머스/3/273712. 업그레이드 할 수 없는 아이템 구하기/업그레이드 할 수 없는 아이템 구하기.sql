select i.item_id, i.item_name, i.rarity
from item_info as i 
left join item_tree as t on t.parent_item_id = i.item_id
where t.parent_item_id is null
order by 1 desc 