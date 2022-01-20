/* Write your T-SQL query statement below */
SELECT
    e.name AS Employee
FROM Employee e, Employee m

WHERE e.salary > m.salary AND e.managerId = m.id
