select HISTORY_ID, CAR_ID, 
    date_format(start_date,'%Y-%m-%d') as START_DATE,
    date_format(end_date,'%Y-%m-%d') as END_DATE,
    case 
        when timestampdiff(day,start_date,end_date) >= 29 then '장기 대여'
        else '단기 대여'
    end as RENT_TYPE
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where year(start_date) = 2022 and month(start_date) = 9
order by 1 desc