import pandas as pd

def _remove_col(data, col_to_rem):
    # we'll only store OHLCV values with date timestamp
    for val in data:
        for col in col_to_rem:
            data[val].pop(col)
    return data

def clean_data(data):
    # remove cols
    col_to_rem = ['Dividends', 'Stock Splits']
    data = _remove_col(data, col_to_rem)

    # uncomment to see if cols were removed
    # print(f'After col remove:\n{data['AAPL']}')

    return data
    

    
    

