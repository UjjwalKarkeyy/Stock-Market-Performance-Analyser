CREATE OR REPLACE VIEW top_five_stock_vol AS 
SELECT
    ticker,
    sum(volume) AS total_vol
FROM
    ohlcv AS o
GROUP BY ticker
ORDER BY sum(volume) DESC 
LIMIT 5;


