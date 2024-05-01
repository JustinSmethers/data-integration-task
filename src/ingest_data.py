import duckdb

# Connect to a database file called task.db
con = duckdb.connect('task.db')

con.sql("CREATE OR REPLACE TABLE content AS (SELECT * FROM read_csv_auto('content.csv'))")
con.sql("CREATE OR REPLACE TABLE membership AS (SELECT * FROM read_csv_auto('membership.csv'))")
con.sql("CREATE OR REPLACE TABLE roles AS (SELECT * FROM read_csv_auto('roles.csv'))")
con.sql("CREATE OR REPLACE TABLE usage AS (SELECT * FROM read_csv_auto('usage.csv'))")
con.sql("CREATE OR REPLACE TABLE usage_incremental_0 AS (SELECT * FROM read_csv_auto('usage_incremental_0.csv'))")
con.sql("CREATE OR REPLACE TABLE usage_incremental_1 AS (SELECT * FROM read_csv_auto('usage_incremental_1.csv'))")

print(con.sql('show all tables'))