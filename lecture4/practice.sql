-- 1
SELECT * FROM flights 
    WHERE origin = 'New York';

-- 2 "Comparison"
SELECT * FROM flights 
    WHERE duration > 500;

-- 3 "AND"
SELECT * FROM flights 
    WHERE duration > 430 
    AND destination = 'Paris';

-- 4 "OR"
SELECT * FROM flights 
    WHERE duration > 500 
    OR destination = 'Paris';

-- 5 "IN"
SELECT * FROM flights 
    WHERE origin IN ('New York', 'Lima');

-- 6 "LIKE" "%a%"
SELECT * FROM flights 
    WHERE origin LIKE '%a%';

-- 7 UPDATE
UPDATE flights
    SET duration = 430
    WHERE origin = 'New York'
    AND destination = 'London';

-- 8 DELETE 
DELETE FROM flights WHERE destination = 'Tokyo';

-- 9 LIMIT
SELECT * FROM flights LIMIT 3;

-- 10 ORDER BY
SELECT * FROM flights ORDER BY duration ASC;

SELECT * FROM flights ORDER BY origin DESC;

-- 11 GROUP BY
SELECT * FROM flights GROUP BY origin;