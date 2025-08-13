select c.id, c.genotype, p.genotype as parent_genotype
from ecoli_data as c
join ecoli_data as p on p.id = c.parent_id
where (p.genotype & c.genotype) = p.genotype
order by 1 asc 