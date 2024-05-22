-- https://leetcode.com/problems/classes-more-than-5-students/

SELECT
    c.class
FROM
    Courses c
GROUP BY
    c.class
HAVING 
    count(c.class) >= 5;