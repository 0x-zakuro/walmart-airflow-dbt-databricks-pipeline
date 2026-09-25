import pandas as pd
from sqlalchemy import create_engine

# Neon connection
engine = create_engine(
    "postgresql+psycopg2://walmart_db_owner:npg_D1s9HIJnzuta@ep-restless-dew-b3k2upgh-pooler.c-4.ap-southeast-1.aws.neon.tech/walmart_db?sslmode=require"
)

# Map each CSV to the table name you want in Postgres
files = {
    "customers": "walmart_dataset/data/customers.csv",
    "employees": "walmart_dataset/data/employees.csv",
    "order_items": "walmart_dataset/data/order_items.csv",
    "orders": "walmart_dataset/data/orders.csv",
    "products": "walmart_dataset/data/products.csv",
    "stores": "walmart_dataset/data/stores.csv",
}

for table_name, path in files.items():
    df = pd.read_csv(path)
    df.to_sql(table_name, engine, if_exists="replace", index=False)
    print(f"Loaded {len(df)} rows into '{table_name}'")

print("All done!")