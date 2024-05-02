import duckdb
import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Navigate to the project base dir, then to the data/ folder 
data_path = os.path.normpath(os.path.join(script_dir, '..', 'data'))

print(data_path)

# Connect to a database file called task.db
con = duckdb.connect(os.path.join(data_path, 'task_db.db'))

# Specify path to raw csv data in data/raw/
content_csv = os.path.join(data_path, 'raw', 'content.csv')
membership_csv = os.path.join(data_path, 'raw', 'membership.csv')
roles_csv = os.path.join(data_path, 'raw', 'roles.csv')
usage_csv = os.path.join(data_path, 'raw', 'usage.csv')
usage_incremental_0_csv = os.path.join(data_path, 'raw', 'usage_incremental_0.csv')
usage_incremental_1_csv = os.path.join(data_path, 'raw', 'usage_incremental_1.csv')

# Load the CSV files into DuckDB as tables
con.sql(f"CREATE OR REPLACE TABLE content AS (SELECT * FROM read_csv_auto('{content_csv}'))")
con.sql(f"CREATE OR REPLACE TABLE membership AS (SELECT * FROM read_csv_auto('{membership_csv}'))")
con.sql(f"CREATE OR REPLACE TABLE roles AS (SELECT * FROM read_csv_auto('{roles_csv}'))")
con.sql(f"CREATE OR REPLACE TABLE usage AS (SELECT * FROM read_csv_auto('{usage_csv}'))")
con.sql(f"CREATE OR REPLACE TABLE usage_incremental_0 AS (SELECT * FROM read_csv_auto('{usage_incremental_0_csv}'))")
con.sql(f"CREATE OR REPLACE TABLE usage_incremental_1 AS (SELECT * FROM read_csv_auto('{usage_incremental_1_csv}'))")

print(con.sql('show all tables'))
