def transform_data(df):
    # Example transformations (safe defaults)
    df.columns = [c.lower() for c in df.columns]
    df = df.drop_duplicates()
    return df
