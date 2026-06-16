import pandas as pd
from pathlib import Path

def remove_timezone(df):
    for col in df.columns:
        if pd.api.types.is_datetime64tz_dtype(df[col]):
            df[col] = df[col].dt.tz_localize(None)
    return df

def generate_xl_report(cur):
    views = [
        'bullish_or_bearish',
        'v_ticker_clv_trends',
        'top_five_stock_vol'
    ]

    output_path = Path("output/market_pulse_report.xlsx")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
            for view in views:
                query = f"SELECT * FROM {view};"

                cur.execute(query)
                rows = cur.fetchall()

                columns = [desc[0] for desc in cur.description]
                df = pd.DataFrame(rows, columns=columns)

                df = remove_timezone(df)

                # uncomment to see the output in terminal
                # print(f"\n--- {view} ---")
                # print(df)

                df.to_excel(
                    writer,
                    sheet_name=view[:31],
                    index=False
                )

        print(f"\nExcel report generated: {output_path}")
    except Exception as e:
        raise e