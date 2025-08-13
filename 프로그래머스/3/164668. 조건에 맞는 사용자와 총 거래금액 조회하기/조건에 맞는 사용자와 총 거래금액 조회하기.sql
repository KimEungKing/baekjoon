SELECT u.user_id, u.nickname, sum(price) as total_sales
from used_goods_board as b
join used_goods_user as u on b.writer_id = u.user_id
where b.status = 'done'
group by u.user_id
having sum(price) >= 700000
order by 3 asc 