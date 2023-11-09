-- We don't care to have the process_id is same row, because the result will be the same in final
SELECT ActivityStart.machine_id, ROUND(AVG(ActivityEnd.timestamp - ActivityStart.timestamp), 3) AS processing_time
FROM Activity AS ActivityStart
INNER JOIN Activity ActivityEnd
ON ActivityStart.machine_id = ActivityEnd.machine_id
WHERE ActivityStart.activity_type = 'start' AND ActivityEnd.activity_type = 'end'
GROUP BY ActivityStart.machine_id;

-- SELECT ActivityStart.machine_id, ROUND(AVG(ActivityEnd.timestamp - ActivityStart.timestamp), 3) AS processing_time
-- FROM Activity AS ActivityStart
-- INNER JOIN Activity ActivityEnd
-- ON ActivityStart.machine_id = ActivityEnd.machine_id AND ActivityStart.process_id = ActivityEnd.process_id AND ActivityStart.activity_type = 'start' AND ActivityEnd.activity_type = 'end'
-- GROUP BY ActivityStart.machine_id;