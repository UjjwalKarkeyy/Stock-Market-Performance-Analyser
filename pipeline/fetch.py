'''
yfinance is a popular Python library that allows users to fetch financial data from Yahoo Finance. 
It provides an easy-to-use interface for retrieving historical market data, stock information, and other financial metrics. 
The library is widely used for data analysis, trading strategies, and financial research.
'''

'''
TICKER INFO:

- AAPL: Apple Inc. - Technology company known for its consumer electronics and software.
- MSFT: Microsoft Corporation - Technology company specializing in software, hardware, and cloud services.
- GOOGL: Alphabet Inc. - Parent company of Google, involved in various technology and
internet-related services.
- AMZN: Amazon.com, Inc. - E-commerce and cloud computing giant.
- JPM: JPMorgan Chase & Co. - Multinational investment bank and financial services company.
- PFE: Pfizer Inc. - Pharmaceutical company known for developing and manufacturing medications and vaccines.
- XOM: Exxon Mobil Corporation - Multinational oil and gas corporation.
- TSLA: Tesla, Inc. - Electric vehicle and clean energy company.
'''
ticker = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'JPM', 'PFE', 'XOM', 'TSLA']

import datetime
import yfinance as yf

def fetch_data():
    # getting the historical data (OHLCV) for 1 year
    start_date = datetime.datetime(2025, 5, 1)
    end_date = datetime.datetime(2026, 5, 1)

    # store OHLCV for each ticker in a dictionary
    data = {}
    for t in ticker:
        new_tick = yf.Ticker(t)
        info = new_tick.history(start=start_date, end=end_date)
        data[t] = info

    # uncomment to see if its working
    print(data['AAPL'])
    return data