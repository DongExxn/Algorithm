-- 코드를 작성해주세요

select count(*) as FISH_COUNT, b.FISH_NAME
from FISH_NAME_INFO b 
join FISH_INFO a on a.FISH_TYPE = b.FISH_TYPE
group by b.FISH_NAME
order by 1 desc