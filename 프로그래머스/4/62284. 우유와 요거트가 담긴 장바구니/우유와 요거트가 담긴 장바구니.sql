select cart_id
from cart_products 
group by cart_id
having GROUP_CONCAT(name SEPARATOR ', ') like '%Yogurt%' and
    GROUP_CONCAT(name SEPARATOR ', ') like '%Milk%'
order by 1 