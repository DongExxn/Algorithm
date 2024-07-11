select a.ID, b.FISH_NAME, a.LENGTH 
from FISH_INFO a
join FISH_NAME_INFO b on a.FISH_TYPE = b.FISH_TYPE
WHERE (a.FISH_TYPE, a.LENGTH) IN (
    SELECT FISH_TYPE, MAX(LENGTH)
    FROM FISH_INFO
    GROUP BY FISH_TYPE
)
order by 1 
