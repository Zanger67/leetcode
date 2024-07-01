CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  SET N = N - 1;
  RETURN (
      # Write your MySQL query statement below.
       SELECT DISTINCT e.salary FROM Employee e ORDER BY e.salary DESC LIMIT N, 1
  );
END