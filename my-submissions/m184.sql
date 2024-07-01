# Write your MySQL query statement below
SELECT d.name as 'Department',
        e.name as 'Employee',
        salary as 'Salary'
FROM Employee e RIGHT OUTER JOIN Department d ON e.departmentId = d.id
WHERE salary = (SELECT max(salary) FROM Employee WHERE Employee.departmentId = e.departmentId)