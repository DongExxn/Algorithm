SELECT 
    A.APNT_NO, 
    P.PT_NAME, 
    P.PT_NO, 
    A.MCDP_CD, 
    D.DR_NAME, 
    A.APNT_YMD
FROM 
    APPOINTMENT A
JOIN 
    PATIENT P ON A.PT_NO = P.PT_NO
JOIN 
    DOCTOR D ON A.MDDR_ID = D.DR_ID
WHERE 
    DATE(A.APNT_YMD) = '2022-04-13'  -- 진료 예약일이 2022년 4월 13일인 경우
    AND A.APNT_CNCL_YN = 'N'         -- 예약 취소 여부가 'N' (취소되지 않은 경우)
    AND A.MCDP_CD = 'CS'             -- 진료 과 코드가 흉부외과(CS)인 경우
ORDER BY 
    A.APNT_YMD ASC;                  -- 진료 예약 일시 기준으로 오름차순 정렬
