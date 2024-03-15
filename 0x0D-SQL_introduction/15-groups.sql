-- using group by to get same score
-- in second_table
SELECT score, COUNT(*)
FROM second_table
GROUP BY score;
