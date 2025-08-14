SELECT car_id, 
    round(avg(timestampdiff(day,start_date,end_date)+1),1) as average_duration
from car_rental_company_rental_history
group by car_id
having average_duration >= 7
order by 2 desc, 1 desc