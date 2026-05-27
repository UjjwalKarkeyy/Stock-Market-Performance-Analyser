from pipeline.fetch import fetch_data
from pipeline.clean import clean_data
from pipeline.load import load_sql
from decorators.progress_bar import progress_bar
from config import create_conn

# using dunder attribute, the below portion only runs if this script itself is executed somehow
if __name__ == '__main__':
    # fetch data for desired tickers
    data = fetch_data()

    # cleaning the data
    cleaned_data = clean_data(data)

    # psql conn for loading data
    try:
        cur, conn = create_conn()
        print(f'PSQL CONN SUCCESSFUL!!!')
        # load data to psql
        load_sql(cleaned_data, cur, conn)

    except Exception as err:
        print(f'Error connecting to PSQL: {err}')

        
