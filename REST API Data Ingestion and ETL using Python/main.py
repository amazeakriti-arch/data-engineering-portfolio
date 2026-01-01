from extract_api import fetch_products
from transform_json import transform
from load_csv import load_csv
from load_db import load_to_db

def run_etl():
    raw_data = fetch_products()
    df = transform(raw_data)
    load_csv(df)
    load_to_db(df)

if __name__ == "__main__":
    run_etl()
