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
