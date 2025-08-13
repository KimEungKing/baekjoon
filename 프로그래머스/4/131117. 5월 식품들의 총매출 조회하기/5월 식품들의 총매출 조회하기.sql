select p.product_id, p.product_name, sum(p.price * o.amount) as total_sales
from food_product as p
join food_order as o on p.product_id = o.product_id
where year(o.produce_date) = 2022 and month(o.produce_date) = 5
group by o.product_id 
order by 3 desc, 1 asc 