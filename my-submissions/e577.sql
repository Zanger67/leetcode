SELECT name, bonus
    FROM Employee e LEFT OUTER JOIN Bonus b ON e.empId = b.empId
    WHERE IFNULL(bonus, 0) < 1000;