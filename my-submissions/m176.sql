# https://leetcode.com/problems/second-highest-salary/description/


SELECT IFNULL(
    (SELECT DISTINCT salary
        FROM Employee e
        ORDER BY salary DESC
        LIMIT 1 OFFSET 1),
    NULL) 
    AS 'SecondHighestSalary';