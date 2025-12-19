from extract import extract_data
from transform import transform_data

OUTPUT_PATH = "output/d3_data.csv"

def load_to_csv(df):
    df.to_csv(OUTPUT_PATH, index=False)
    print("Data written to CSV")

if __name__ == "__main__":
    df = extract_data()
    df = transform_data(df)
    load_to_csv(df)