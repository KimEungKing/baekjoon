select year(differentiation_date) as year, 
    (MAX(size_of_colony) OVER (PARTITION BY YEAR(differentiation_date)) - size_of_colony) as year_dev,
    id 
from ecoli_data
order by 1 asc, 2 asc