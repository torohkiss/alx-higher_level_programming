-- using group by to get same num in second_table
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score DESC;
