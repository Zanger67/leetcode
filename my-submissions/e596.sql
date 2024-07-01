SELECT
    c.class
FROM
    Courses c
GROUP BY
    c.class
HAVING 
    count(c.class) >= 5;