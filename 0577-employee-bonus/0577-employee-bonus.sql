# Write your MySQL query statement below

select name,bonus from employee as e left join bonus as b on e.empId=b.empId WHERE b.bonus<1000 or b.bonus is null;