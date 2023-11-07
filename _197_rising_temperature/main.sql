# Write your MySQL query statement below
SELECT Weather.id FROM Weather weather, Weather weatherYesterday
WHERE DATEDIFF(weather.recordDate, weatherYesterday.recordDate) = 1
AND weatherYesterday.temperature < weather.temperature