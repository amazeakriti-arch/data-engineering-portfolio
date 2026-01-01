OUTPUT_PATH = "output/products.csv"
def load_csv(df):
    df.to_csv(OUTPUT_PATH, index=False)