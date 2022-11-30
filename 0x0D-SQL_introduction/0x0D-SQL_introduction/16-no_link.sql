-- Lists all the records of the table second_table having a name value.
-- Records are ordered by the descending score.
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
