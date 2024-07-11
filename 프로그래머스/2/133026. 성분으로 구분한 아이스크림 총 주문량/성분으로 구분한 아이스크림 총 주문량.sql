-- 코드를 입력하세요
SELECT b.INGREDIENT_TYPE, SUM(a.TOTAL_ORDER) as TOTAL_ORDER
from FIRST_HALF a
JOIN ICECREAM_INFO b ON a.FLAVOR = b.FLAVOR
group by b.INGREDIENT_TYPE
order by TOTAL_ORDER