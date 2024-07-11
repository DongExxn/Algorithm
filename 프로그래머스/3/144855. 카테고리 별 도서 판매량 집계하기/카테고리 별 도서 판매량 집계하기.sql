-- 코드를 입력하세요
select B.CATEGORY, sum(SUM_TOTAL) as TOTAL_SALES
from BOOK B
join
(SELECT S.BOOK_ID, sum(S.SALES) as SUM_TOTAL
from BOOK_SALES S
where month(S.SALES_DATE) = 1 and year(S.SALES_DATE) = 2022
group by S.BOOK_ID) S
on B.BOOK_ID = S.BOOK_ID
group by B.CATEGORY
order by 1