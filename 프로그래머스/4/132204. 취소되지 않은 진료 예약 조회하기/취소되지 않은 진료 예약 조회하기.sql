-- 진료예약번호, 환자이름, 환자번호, 진료과코드, 의사이름, 진료예약일시 항목
select a.apnt_no, p.pt_name, a.pt_no, a.mcdp_cd, d.dr_name, a.apnt_ymd
from appointment as a 
join patient as p on p.pt_no = a.pt_no
join doctor as d on d.dr_id = a.mddr_id
where year(a.apnt_ymd) = 2022 and 
    month(a.apnt_ymd) = 4 and
    day(a.apnt_ymd) = 13 and a.apnt_cncl_yn = 'N'
order by 6 asc 