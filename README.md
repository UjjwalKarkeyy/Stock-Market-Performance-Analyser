# MarketPulse

MarketPulse is a short, Python-first stock market pipeline project. Its purpose is to practice a realistic data workflow, not to present a deep financial analysis.

The project uses Python to fetch and clean Yahoo Finance data, PostgreSQL to store and query the data, and Excel as the final reporting output. One command runs the full workflow from data extraction to workbook generation.

## Project Focus

This project is Step 3 in a structured data analytics portfolio roadmap. The emphasis is on pipeline automation:

```text
fetch -> clean -> load -> query -> export
```

Each tool is used for the job it fits best:

- Python handles data extraction, cleaning, and orchestration.
- PostgreSQL stores the OHLCV data and exposes reusable SQL views.
- Excel receives the final generated report through `openpyxl`.

## Tech Stack

- Python
- yfinance
- pandas
- PostgreSQL
- psycopg2
- openpyxl
- python-dotenv

## Data

The pipeline fetches one year of daily OHLCV stock data from Yahoo Finance using `yfinance`.

The configured ticker list is maintained in [pipeline/fetch.py](pipeline/fetch.py).

The portfolio brief for this project targets the following stock universe:

```text
AAPL, MSFT, GOOGL, AMZN, JPM, GS, JNJ, PFE, XOM, TSLA
```

## Project Structure

```text
.
|-- main.py                  # Runs the full pipeline
|-- config.py                # PostgreSQL connection setup
|-- pipeline/
|   |-- fetch.py             # Fetches Yahoo Finance data
|   |-- clean.py             # Removes unused columns
|   `-- load.py              # Loads cleaned data into PostgreSQL
|-- sql/
|   |-- schema.sql           # Base table definition
|   `-- Scripts/             # SQL views used by the report
|-- report/
|   `-- generate_report.py   # Exports SQL view results to Excel
|-- output/
|   `-- market_pulse_report.xlsx
`-- requirements.txt
```

## SQL Outputs

The Excel report is generated from three PostgreSQL views:

- `bullish_or_bearish`
- `v_ticker_clv_trends`
- `top_five_stock_vol`

These views keep the reporting logic in SQL while Python handles orchestration and export.

## Setup

1. Create and activate a virtual environment.

```bash
python -m venv .venv
```

2. Install dependencies.

```bash
pip install -r requirements.txt
```

3. Create a `.env` file with PostgreSQL connection settings.

```env
HOST=localhost
DB=db_name
USER=your_user
PASS=your_password
PORT=5432
```

4. Create the database table and SQL views in PostgreSQL.

Run [sql/schema.sql](sql/schema.sql), then run the scripts in [sql/Scripts](sql/Scripts).

## Run

```bash
python main.py
```

The pipeline will:

1. Fetch stock data from Yahoo Finance.
2. Remove unused columns.
3. Load OHLCV data into PostgreSQL.
4. Query the SQL views.
5. Generate the Excel workbook at [output/market_pulse_report.xlsx](output/market_pulse_report.xlsx).

## Portfolio Roadmap

| Step | Tool | Project | Status |
| --- | --- | --- | --- |
| 1 | SQL | Retail360, Olist and PostgreSQL | Done |
| 2 | Excel | PeopleMetrics, IBM HR Analytics | Done |
| 3 | Python | MarketPulse, yfinance pipeline | This project |
| 4 | Power BI | Dashboard from Steps 1, 2, or 3 | Next |
| 5 | Pipeline | Airflow, dbt, and AWS S3 | Upcoming |
| 6 | ML | Classical algorithms and prediction | Upcoming |
| 7 | Capstone | Full pipeline with real-time ML | Upcoming |

## Notes

MarketPulse is intentionally concise. The main value is the automated workflow across Python, SQL, and Excel rather than the depth of stock market analysis. Visualization is intentionally deferred to the next portfolio step.
