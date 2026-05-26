-- example 1: Top 5 largest market caps

SELECT
    name,
    market_cap
FROM crypto_market
ORDER BY market_cap DESC
LIMIT 5;

-- example 2: Biggest positive daily movers

SELECT
    name,
    price_change_24h
FROM crypto_market
ORDER BY price_change_24h DESC
LIMIT 5;

-- example 3:
-- Write a query that returns:
-- the latest record for each cryptocurrency
-- based on the newest extracted_at
-- Output:
-- symbol
-- current_price
-- extracted_at

WITH ranked_symb AS(
    SELECT 
        symbol, current_price, extracted_at,
        ROW_NUMBER() OVER(
            PARTITION BY symbol
            ORDER BY extracted_at DESC
        ) AS rn
    FROM crypto_market
) SELECT symbol, current_price, extracted_at FROM ranked_symb 
WHERE rn = 1;


-- example 4:
-- For each extraction_date, calculate:
-- average current price
-- maximum current price
-- minimum current price
-- Sort by extraction_date asce

SELECT extraction_date, AVG(current_price) AS avg_price, 
MIN(current_price) AS min_price, MAX(current_price) AS max_price
FROM crypto_market 
GROUP BY extraction_date
ORDER BY extraction_date ASC;


-- example 5:
-- For each cryptocurrency:
-- compare today’s price with previous day’s price
-- calculate price difference
-- Output:
-- symbol
-- extraction_date
-- current_price
-- previous_price
-- price_difference

-- look at week2proj-notes.md in the mistakes section
-- WITH price_analysis AS(
--     SELECT symbol, extraction_date, current_price,
--     LAG(current_price) OVER
--     (
--         PARTITION BY symbol
--         ORDER BY extraction_date ASC
--     ) AS previous_price, 
--     (current_price - LAG(current_price) OVER (PARTITION BY symbol
--     ORDER BY extraction_date ASC)) AS previous_difference
--     FROM crypto_market 
-- ) SELECT * FROM price_analysis ORDER BY symbol, extraction_date;

-- corrected and improved:
WITH price_analysis AS (
    SELECT
        symbol,
        extraction_date,
        extraction_time,
        current_price,

        LAG(current_price) OVER (
            PARTITION BY symbol
            ORDER BY extraction_date, extracted_at
        ) AS previous_price

    FROM crypto_market
)

SELECT
    symbol,
    extraction_date,
    extraction_time,
    current_price,
    previous_price,
    current_price - previous_price AS price_difference
FROM price_analysis
ORDER BY symbol, extraction_date, extracted_at;