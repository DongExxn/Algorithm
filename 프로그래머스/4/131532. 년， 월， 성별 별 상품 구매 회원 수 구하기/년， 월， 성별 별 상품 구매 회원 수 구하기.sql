-- 코드를 입력하세요
SELECT year(SALES_DATE) as YEAR, MONTH(SALES_DATE) as MONTH, GENDER, count(distinct o.USER_ID) as USERS
from USER_INFO as u  join ONLINE_SALE as o
on o.USER_ID = u.USER_ID
where GENDER is not NULL
group by year(SALES_DATE), MONTH(SALES_DATE), GENDER
order by year(SALES_DATE), MONTH(SALES_DATE), GENDER