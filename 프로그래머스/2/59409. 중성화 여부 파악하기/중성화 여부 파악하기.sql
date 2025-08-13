SELECT animal_id, name, 
    if(sex_upon_intake like 'Neu%' or sex_upon_intake like 'Spay%','O','X')
from animal_ins
order by 1 