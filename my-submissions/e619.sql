# https://leetcode.com/problems/biggest-single-number/description/


SELECT 
    MAX(num) AS 'num'
FROM (
    SELECT num
    FROM MyNumbers mn
    GROUP BY num
    HAVING COUNT(num) = 1
) AS unique_vals;