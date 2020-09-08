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

### 181. Employees Earning More Than Their Managers
-  `JOIN ON`

```sql

SELECT a.Name as Employee
FROM Employee a JOIN Employee b
ON a.ManagerId = b.Id
WHERE a.Salary > b.Salary ;

```

### 1179. Reformat Department Table
- `CASE WHEN THEN ELSE END` syntax
- `MAX` as Agg function make one record in one row



```sql

# Write your MySQL query statement below
SELECT id, 
MAX(CASE WHEN month='Jan' then revenue ELSE NULL END) AS Jan_Revenue,
MAX(CASE WHEN month='Feb' then revenue ELSE NULL END) AS Feb_Revenue,
MAX(CASE WHEN month='Mar' then revenue ELSE NULL END) AS Mar_Revenue,
MAX(CASE WHEN month='Apr' then revenue ELSE NULL END) AS Apr_Revenue,
MAX(CASE WHEN month='May' then revenue ELSE NULL END) AS May_Revenue,
MAX(CASE WHEN month='Jun' then revenue ELSE NULL END) AS Jun_Revenue,
MAX(CASE WHEN month='Jul' then revenue ELSE NULL END) AS Jul_Revenue,
MAX(CASE WHEN month='Aug' then revenue ELSE NULL END) AS Aug_Revenue,
MAX(CASE WHEN month='Sep' then revenue ELSE NULL END) AS Sep_Revenue,
MAX(CASE WHEN month='Oct' then revenue ELSE NULL END) AS Oct_Revenue,
MAX(CASE WHEN month='Nov' then revenue ELSE NULL END) AS Nov_Revenue,
MAX(CASE WHEN month='Dec' then revenue ELSE NULL END) AS Dec_Revenue

FROM Department
GROUP BY id
ORDER BY id ;
```

### 626. Exchange Seats
- `MOD()` 
- usage of commas

```sql
SELECT 
(CASE
    WHEN MOD(id,2)!=0 and counts != id THEN id+1
    WHEN MOD(id,2)!=0 and counts = id THEN id
    ELSE id-1 END
) AS id,
    student
FROM seat,
    (
        SELECT COUNT(*) as counts
        FROM seat
    ) as seat_counts
    
ORDER BY id;


```


### 1270. All People Report to the Given Manager

```sql

# Write your MySQL query statement below
SELECT e1.employee_id
FROM Employees e1
JOIN Employees e2 ON e1.manager_id = e2.employee_id
JOIN Employees e3 ON e2.manager_id = e3.employee_id 
WHERE e3.manager_id=1 AND  e1.employee_id != 1


```