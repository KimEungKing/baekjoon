select a.author_id, a.author_name, b.category, sum(b.price* s.sales) as total_sales
from book as b
join author as a on b.author_id = a.author_id
join book_sales as s on b.book_id = s.book_id
where year(sales_date) = 2022 and month(sales_date) = 1 
group by a.author_id, category
order by 1 asc, 3 desc