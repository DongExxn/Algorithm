SELECT 
    YEAR(A.DIFFERENTIATION_DATE) AS YEAR,
    ABS(A.SIZE_OF_COLONY - B.MAX_SIZE) AS YEAR_DEV,
    A.ID
FROM 
    ECOLI_DATA A
inner JOIN (
    SELECT 
        YEAR(DIFFERENTIATION_DATE) AS YEAR,
        MAX(SIZE_OF_COLONY) AS MAX_SIZE
    FROM 
        ECOLI_DATA
    GROUP BY 
        YEAR(DIFFERENTIATION_DATE)
) B
ON 
    YEAR(A.DIFFERENTIATION_DATE) = B.YEAR
ORDER BY 
    YEAR ASC,
    YEAR_DEV ASC,
    A.ID ASC;
