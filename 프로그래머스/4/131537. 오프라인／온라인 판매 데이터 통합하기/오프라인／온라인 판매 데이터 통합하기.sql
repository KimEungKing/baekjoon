select date_format(sales_date,'%Y-%m-%d'), product_id, user_id, sum(sales_amount)
from (SELECT sales_date, product_id, user_id, sales_amount
    from online_sale
    where month(sales_date) = 3
    union all
    select sales_date, product_id, null as user_id, sales_amount
    from offline_sale
    where month(sales_date) = 3) as a 
group by sales_date, product_id, user_id
order by 1, 2, 3