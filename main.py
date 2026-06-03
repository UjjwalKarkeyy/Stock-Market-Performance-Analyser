from pipeline.fetch import fetch_data
from pipeline.clean import clean_data
from pipeline.load import load_sql
from decorators.progress_bar import progress_bar
from config import create_conn
import pandas as pd
import time

# using dunder attribute, the below portion only runs if this script itself is executed somehow
if __name__ == '__main__':
    # fetch data for desired tickers
    delay = progress_bar(task_name='FETCHING DATA')
    data = fetch_data()
    time.sleep(delay)

    # cleaning the data
    delay = progress_bar(task_name='CLEANING DATA')
    cleaned_data = clean_data(data)
    time.sleep(delay)

    # psql conn for loading data
    delay = progress_bar(task_name='LOADING DATA')
    try:
        cur, conn = create_conn()
        # uncomment to check if PSQL connected successfully
        # print(f'PSQL CONN SUCCESSFUL!!!')
        # load data to psql
        load_sql(cleaned_data, cur, conn, pd)
        time.sleep(delay)
        print('ALL TASKS SUCCESSFULLY COMPLETED!!!')

    except Exception as err:
        print(f'Error connecting to PSQL: {err}')
  
