-- 코드를 작성해주세요
SELECT count(*) as COUNT
FROM ECOLI_DATA
WHERE (GENOTYPE & 2) != 2 
                 AND ((GENOTYPE & 4) = 4 OR (GENOTYPE & 1) = 1)