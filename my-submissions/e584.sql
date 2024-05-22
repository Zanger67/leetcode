-- https://leetcode.com/problems/find-customer-referee/

SELECT
    c.name
FROM
    Customer c
WHERE
    IFNULL(c.referee_id, 0) <> 2;