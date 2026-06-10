CREATE OR REPLACE VIEW v_ticker_clv_trends AS 
SELECT
    ticker,
    trade_date,
    open_val,
    high,
    low,
    close_val,
    CASE
        WHEN ROUND(high::numeric, 2) = ROUND(low::numeric, 2) THEN 0
        ELSE ((close_val - low) - (high - close_val)) / (high - low)
    END AS instant_trend_score,
    CASE
        WHEN ROUND(high::numeric, 2) = ROUND(low::numeric, 2) THEN 'FLAT / NO MOTION'
        WHEN ((close_val - low) - (high - close_val)) / (high - low) >= 0.5 THEN 'STRONG BULLISH'
        WHEN ((close_val - low) - (high - close_val)) / (high - low) <= -0.5 THEN 'STRONG BEARISH'
        ELSE 'NEUTRAL / CHOPPY'
    END AS trend_signal
FROM ohlcv AS o
ORDER BY ticker ASC, trade_date ASC;