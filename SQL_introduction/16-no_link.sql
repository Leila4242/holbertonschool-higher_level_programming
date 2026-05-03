-- Lists the number of records with the same score,
-- but only for rows where the name is not empty (NULL).
-- Results are ordered by the number of records (descending).
SELECT score, COUNT(*) AS number
FROM second_table
WHERE name IS NOT NULL
GROUP BY score
ORDER BY number DESC;
