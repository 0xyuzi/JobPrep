# Leetcode SQL Problems

### 185. Department Top Three Salaries
- `dense_rank() over`
- `partition by` 

```sql

SELECT d.Name as Department, a.Name as Employee, a.Salary
FROM
(
    SELECT e.*, DENSE_RANK() OVER (PARTITION BY e.DepartmentId ORDER BY e.Salary DESC) AS DeptSalRank
    FROM Employee e
) a

JOIN Department d
ON d.Id = a.DepartmentId
WHERE DeptSalRank <=3
```


### 262. Trips and Users
- Join two tables on `Users_Id` and `Client_Id` and `Driver_Id` with condition `Banned !=No`
- `AVG(status!='completed')` and `GROUP BY` `Request_at`

```sql
SELECT t.Request_at AS DAy , ROUND(AVG(t.Status!='completed'),2) AS 'Cancellation Rate'
FROM trips t JOIN Users u1 ON (u1.Users_Id = t.Client_Id AND u1.Banned ='NO')
             JOIN Users u2 on (u2.Users_Id = t.Driver_Id AND u2.Banned = 'NO')
WHERE t.Request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY t.Request_at
```