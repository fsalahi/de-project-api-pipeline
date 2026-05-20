-- Top 5 largest market caps

SELECT
    name,
    market_cap
FROM crypto_market
ORDER BY market_cap DESC
LIMIT 5;

-- Biggest positive daily movers

SELECT
    name,
    price_change_24h
FROM crypto_market
ORDER BY price_change_24h DESC
LIMIT 5;



