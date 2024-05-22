-- https://leetcode.com/problems/sales-person/

SELECT
    sp1.name
FROM 
    SalesPerson sp1
WHERE 
    sp1.name NOT IN (SELECT sp2.name 
                        FROM SalesPerson sp2 
                            LEFT JOIN Orders o ON sp2.sales_id = o.sales_id 
                            LEFT JOIN Company c ON o.com_id = c.com_id
                        WHERE
                            c.name = 'RED')