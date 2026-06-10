CREATE OR REPLACE VIEW bullish_or_bearish AS 
WITH avg_open_close AS(
SELECT
    ticker,
    avg(open_val) AS avg_open,
    avg(close_val) AS avg_close
FROM
    ohlcv AS o  
GROUP BY ticker
)

SELECT
    aoc.ticker,
    CASE
        WHEN aoc.avg_open > avg_close THEN 'Bearish' 
        WHEN aoc.avg_close > avg_open THEN 'Bullish'
        ELSE 'Equal'
    END AS bullOrBear,
    aoc.avg_open, aoc.avg_close
    
FROM
    avg_open_close AS aoc;
