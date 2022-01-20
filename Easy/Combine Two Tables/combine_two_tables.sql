/* Write your T-SQL query statement below */

SELECT Person.firstName, Person.lastName, Address.state, Address.city
FROM Person

LEFT JOIN Address
ON Person.personId = Address.personId;