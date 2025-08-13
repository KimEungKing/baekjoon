SELECT mcdp_cd as '진료과 코드', count(*) AS '5월예약건수'
FROM APPOINTMENT
where YEAR(APNT_YMD) = 2022 AND MONTH(APNT_YMD) = 5
group by mcdp_cd
ORDER BY 2 ASC, 1 ASC 