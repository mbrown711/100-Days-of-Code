SHOW PROCESSLIST;
	
SET GLOBAL event_scheduler = ON;

SHOW PROCESSLIST;

-- structure for creating event:
-- CREATE EVENT [IF NOT EXIST]  event_name
-- ON SCHEDULE schedule
-- DO
-- event_body

CREATE EVENT IF NOT EXISTS get_times
ON SCHEDULE EVERY 2 WEEK STARTS CURRENT_DATE
DO
  SELECT * FROM Employees;
  --export a csv