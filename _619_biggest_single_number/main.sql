SELECT MAX(num) AS num FROM MyNumbers AS n1 WHERE EXISTS (
    SELECT num FROM MyNumbers AS n2 GROUP BY num HAVING COUNT(num) = 1 AND n1.num = n2.num
)