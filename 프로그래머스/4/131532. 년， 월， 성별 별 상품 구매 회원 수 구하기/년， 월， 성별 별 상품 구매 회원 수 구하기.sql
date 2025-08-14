select year(sales_date) as year,
    month(sales_date) as month,
    gender, count(distinct(u.user_id))
from user_info as u
join online_sale as o on u.user_id = o.user_id 
where gender is not null
group by year, month, gender
order by 1,2,3