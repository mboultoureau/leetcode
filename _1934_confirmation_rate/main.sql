SELECT s.user_id, ROUND(COALESCE(COUNT(c2.time_stamp) / COUNT(c1.time_stamp), 0), 2) AS confirmation_rate
FROM Signups AS s
LEFT JOIN Confirmations AS c1 ON s.user_id = c1.user_id
LEFT JOIN Confirmations AS c2 ON c1.user_id = c2.user_id AND c1.time_stamp = c2.time_stamp AND c2.action = "confirmed"
GROUP BY s.user_id;