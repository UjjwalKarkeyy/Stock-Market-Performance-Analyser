CREATE DATABASE IF NOT EXISTS stock_market_yfinance;

CREATE TABLE IF NOT EXISTS ohlcv(
	ticker varchar(10) not null,
	trade_date timestamp with time zone not null,
	open_val float,
	high float,
	low float,
	close_val float,
	volume float
);


