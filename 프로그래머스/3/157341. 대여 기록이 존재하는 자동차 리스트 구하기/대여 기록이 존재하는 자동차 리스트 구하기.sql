-- 코드를 입력하세요
SELECT distinct(C.CAR_ID)
FROM CAR_RENTAL_COMPANY_CAR as C
inner join CAR_RENTAL_COMPANY_RENTAL_HISTORY as H ON C.CAR_ID = H.CAR_ID
where month(H.START_DATE) = 10 and C.CAR_TYPE = '세단'
order by C.CAR_ID desc