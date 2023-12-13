-- list all records with a score >= 10 in the table second_table in my MYSQL server.
-- Results should display both the score and the name (in this order)
-- Records should be ordered by score (top first)
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC; 
