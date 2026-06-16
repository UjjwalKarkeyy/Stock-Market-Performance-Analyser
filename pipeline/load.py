def _insert_into_psql(df, tick, cur, conn):
    insert_query = """
    INSERT INTO ohlcv (ticker, trade_date, open_val, high, low, close_val, volume)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (ticker, trade_date) DO NOTHING;
    """
    rows = [
        (
            tick,
            row['Date'],
            row['Open'],
            row['High'],
            row['Low'],
            row['Close'],
            row['Volume'],
        )
        for _, row in df.iterrows()
    ]
    try:
        cur.executemany(insert_query, rows)
        conn.commit()
    except Exception as e:
        raise e

def load_sql(data, cur, conn, pd):
    try:
        for tick in data.keys():
            df = pd.DataFrame(data[tick])
            df = df.reset_index()
            _insert_into_psql(df, tick, cur, conn)
    except Exception as e:
        print(f'Exception occurred while loading data to PSQL: {e}')



