select u.item_id, u.item_name, u.rarity
from item_info as p
join item_tree as t on p.item_id = t.parent_item_id
join item_info as u on t.item_id = u.item_id
where p.rarity = 'RARE'
order by 1 desc