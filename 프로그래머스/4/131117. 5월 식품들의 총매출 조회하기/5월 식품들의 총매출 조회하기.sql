-- 코드를 입력하세요
SELECT o.PRODUCT_ID, p.PRODUCT_NAME, sum(p.PRICE * o.AMOUNT) as TOTAL_SALES
from FOOD_ORDER o
join FOOD_PRODUCT p on p.PRODUCT_ID = o.PRODUCT_ID
where  month(o.PRODUCE_DATE) = 5
group by o.PRODUCT_ID
order by 3 desc, 1