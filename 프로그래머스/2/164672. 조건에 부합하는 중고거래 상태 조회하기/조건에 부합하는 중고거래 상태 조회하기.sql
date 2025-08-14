select board_id, writer_id, title, price, 
    case 
        when status = 'SALE' then '판매중'
        when status = 'RESERVED' then '예약중'
        when status = 'DONE' then '거래완료'
    end as 거래상태
from used_goods_board
where year(created_date) = 2022 and
    month(created_date) = 10 and 
    day(created_date) = 5
order by 1 desc 
