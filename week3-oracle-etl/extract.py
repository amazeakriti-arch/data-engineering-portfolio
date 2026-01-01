import pandas as pd
from config import ENGINE

def extract_data():
    query = "SELECT * FROM student_report"
    df = pd.read_sql(query, ENGINE)
    return df

if __name__ == "__main__":
    df = extract_data()
    print("Rows extracted:", len(df))
