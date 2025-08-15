select e.emp_no, e.emp_name, 
    case  
        when avg(g.score) >= 96 then 'S'
        when avg(g.score) >= 90 then 'A'
        when avg(g.score) >= 80 then 'B'
        else 'C'
    end as grade,
    e.sal*(case 
            when avg(g.score) >= 96 then 0.2
            when avg(g.score) >= 90 then 0.15
            when avg(g.score) >= 80 then 0.1
            else 0
        end) as bonus 
from hr_employees as e
join hr_grade as g on e.emp_no = g.emp_no
group by e.emp_no
order by 1 
