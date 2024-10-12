-- 코드를 입력하세요
SELECT U.USER_ID, U.NICKNAME, CONCAT(U.CITY, ' ', U.STREET_ADDRESS1, ' ', IFNULL(U.STREET_ADDRESS2, '')) AS 전체주소, 
       CONCAT(SUBSTRING(U.TLNO, 1, 3), '-', SUBSTRING(U.TLNO, 4, 4), '-', SUBSTRING(U.TLNO, 8, 4)) AS 전화번호
from USED_GOODS_USER as U
join (select WRITER_ID from USED_GOODS_BOARD GROUP BY WRITER_ID HAVING COUNT(*) >= 3) as NEW
on U.USER_ID = NEW.WRITER_ID
order by U.USER_ID desc