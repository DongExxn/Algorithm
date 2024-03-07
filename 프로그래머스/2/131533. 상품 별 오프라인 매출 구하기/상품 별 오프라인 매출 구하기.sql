-- 코드를 입력하세요
SELECT p.PRODUCT_CODE, sum(p.PRICE * o.SALES_AMOUNT) as SALES from PRODUCT p
join OFFLINE_SALE o on p.PRODUCT_ID = O.PRODUCT_ID
group by p.PRODUCT_CODE
order by sales desc, PRODUCT_CODE
