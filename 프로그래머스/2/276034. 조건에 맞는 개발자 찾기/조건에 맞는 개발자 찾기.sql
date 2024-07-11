-- 코드를 작성해주세요

SELECT D.ID, D.EMAIL, D.FIRST_NAME, D.LAST_NAME
FROM DEVELOPERS D
WHERE D.SKILL_CODE & (SELECT S.CODE FROM SKILLCODES S WHERE NAME = 'Python')
    OR D.SKILL_CODE & (SELECT S.CODE FROM SKILLCODES S WHERE NAME = 'C#')
ORDER BY D.ID