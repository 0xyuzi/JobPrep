# Leetcode SQL Problems

### [184. Department Highest Salary](https://leetcode.com/problems/department-highest-salary/)
__Key points__
- `DENSE_RANK() OVER (PARTITION BY ... ORDER BY ... [DESC|ASC])`
- Use `JOIN` here instead of `LEFT JOIN` to prevent if the "Department" table is NULL

``` sql
# Write your MySQL query statement below

# dense_rank 

WITH Dept_rank_salary AS (

    SELECT DepartmentId, Name, salary, DENSE_RANK() OVER(PARTITION BY DepartmentId ORDER BY salary DESC) AS dept_salary_rank
    FROM Employee
    
) 

SELECT t.Name as Department, d.Name AS Employee, d.salary as Salary

FROM Dept_rank_salary as d

JOIN Department t

ON t.id = d.departmentid 

WHERE d.dept_salary_rank = 1

```





### 177. Nth Highest Salary
__Key points__
- `DENSE_RANK() OVER(ORDER BY ... DESC)`, why not use `ROW_NUMBER()` or `RANK()`  here, [example](https://codingsight.com/similarities-and-differences-among-rank-dense_rank-and-row_number-functions/)
- `DISTINCT()` render only 1 result 
- [Great article](https://leetcode-cn.com/problems/nth-highest-salary/solution/mysql-zi-ding-yi-bian-liang-by-luanz/) on different methods and their query efficiency

```sql
      SELECT DISTINCT salary 
      FROM 
      (
        SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) as rank_salary
        FROM Employee
      ) rank_s
      
      WHERE rank_salary=N 

```


### 1468. Calculate Salaries
__Key points__
- CASE WHEN... THEN ... ELSE ... END AS [Example](https://mode.com/sql-tutorial/sql-case/)
- `ROUND` FUNCTION, default round number to integer [example](https://www.w3schools.com/sql/func_sqlserver_round.asp)
- `JOIN ON` and `LEFT JOIN ON`
-  [Common table  expression (CTE)](https://blog.csdn.net/bcbobo21cn/article/details/71155359), `WITH... AS ()`


__Method 1__
``` sql
SELECT s.company_id, s.employee_id, s.employee_name, 
ROUND(s.salary*(1-m.tax_rate)) AS salary
FROM Salaries s

LEFT JOIN (
    SELECT 
    company_id,
    CASE
        WHEN MAX(salary) < 1000 THEN 0
        WHEN MAX(salary) BETWEEN 1000 and 10000 THEN 0.24
        ELSE 0.49
    END AS tax_rate
    FROM Salaries
    GROUP BY company_id
) m

ON m.company_id = s.company_id 
```

__METHOD 2, cte__
```sql

WITH Company_tax AS (

    SELECT company_id, 
        CASE 
            WHEN MAX(salary) < 1000 THEN 0
            WHEN MAX(salary) BETWEEN 1000 AND 10000 THEN 0.24
            WHEN MAX(salary) > 10000 THEN 0.49  
        END AS tax_rate
    
    FROM Salaries
    
    GROUP BY company_id
)




SELECT 
    s.company_id, 
    s.employee_id, 
    s.employee_name, 
    ROUND(s.salary*(1 - t.tax_rate)) AS salary

FROM Salaries s 

LEFT JOIN Company_tax t

ON t.company_id = s.company_id



```


### 176. Second Highest Salary
``` sql
SELECT MAX(Salary) AS SecondHighestSalary 
FROM Employee 
WHERE Salary < (SELECT MAX(Salary) AS max_salary FROM Employee)
```

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

### 196. Delete Duplicate Emails

```sql

DELETE p1 
FROM Person p1, Person p2
WHERE p1.Email = p2.Email AND p1.Id> p2.Id;
```



### 615. Average Salary: Departments VS Company
- [Solution from LC Chinese official website](https://leetcode-cn.com/problems/average-salary-departments-vs-company/solution/ping-jun-gong-zi-bu-men-yu-gong-si-bi-jiao-by-leet/)
- date_format(pay_date,'%Y-%M')


```sql

/* First step: get monthly avg company salary */
/*
SELECT 
    AVG(amount) as company_month_avg_salary, 
    date_format(pay_date, '%Y-%m') AS pay_month
FROM salary
GROUP BY date_format(pay_date, '%Y-%M');

*/

/* Second step: get department monthly avg department salary */
/*
SELECT 
    department_id,
    AVG(amount) as dept_month_avg_salary, 
    date_format(pay_date, '%Y-%m') AS pay_month
    
    
FROM salary s 
JOIN employee e
ON  s.employee_id = e.employee_id 
GROUP BY date_format(pay_date, '%Y-%M'), department_id;

*/

-- Final step: 

SELECT 
    dept_month_salary.pay_month,
    dept_month_salary.department_id,
    (
        CASE 
            WHEN dept_month_avg_salary>company_month_avg_salary THEN 'higher'
            WHEN dept_month_avg_salary = company_month_avg_salary THEN 'same'
            ELSE 'lower' 
        END
    ) AS comparison
    
FROM
    (
        SELECT 
        AVG(amount) as company_month_avg_salary, 
        date_format(pay_date, '%Y-%m') AS pay_month
        FROM salary
        GROUP BY date_format(pay_date, '%Y-%M')
    ) AS company_month_salary
    
    JOIN
    (
        SELECT 
            department_id,
            AVG(amount) as dept_month_avg_salary, 
            date_format(pay_date, '%Y-%m') AS pay_month

            FROM salary s 
            JOIN employee e
            ON  s.employee_id = e.employee_id 
            GROUP BY date_format(pay_date, '%Y-%M'), department_id
    ) AS dept_month_salary
    
    ON dept_month_salary.pay_month = company_month_salary.pay_month;

```


### 180. Consecutive Numbers
- [Solution from LC sql chinese website](https://leetcode-cn.com/problems/consecutive-numbers/solution/lian-xu-chu-xian-de-shu-zi-by-leetcode/)
-  `DISTINCT` to remove the duplicates


```sql

# Write your MySQL query statement below
SELECT DISTINCT l1.Num AS ConsecutiveNums 
FROM
    Logs l1, Logs l2, Logs l3

WHERE 
    l1.Num = l2.Num AND l2.Num = l3.Num
    AND l1.id = l2.id -1 AND l2.id = l3.id -1;


```