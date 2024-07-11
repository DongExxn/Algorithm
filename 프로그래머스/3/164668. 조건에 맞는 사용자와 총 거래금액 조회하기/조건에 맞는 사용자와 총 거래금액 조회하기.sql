-- 코드를 입력하세요
SELECT U.USER_ID, U.NICKNAME, sum(B.PRICE) as TOTAL_SALES
from USED_GOODS_BOARD B
join USED_GOODS_USER U on B.WRITER_ID = U.USER_ID
where B.STATUS = 'DONE'
GROUP BY U.USER_ID, U.NICKNAME
HAVING SUM(B.PRICE) >= 700000
order by 3
