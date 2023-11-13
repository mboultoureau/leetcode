SELECT
    query_name,
    ROUND(AVG(rating / position), 2) AS quality,
    ROUND(AVG(rating < 3) * 100, 2) AS poor_query_percentage
FROM Queries
GROUP BY query_name;

# SELECT
#     query_name,
#     ROUND((SELECT SUM(q3.rating / q3.position) FROM Queries q3 WHERE q1.query_name = q3.query_name) / COUNT(q1.query_name), 2)  AS quality,
#     ROUND((SELECT COUNT(*) FROM Queries AS q2 WHERE q1.query_name = q2.query_name AND q2.rating < 3) / COUNT(q1.query_name) * 100, 2) AS poor_query_percentage
# FROM Queries AS q1
# GROUP BY query_name;