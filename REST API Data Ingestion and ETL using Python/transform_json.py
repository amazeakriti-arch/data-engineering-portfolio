import pandas as pd

def transform(data):
    df = pd.json_normalize(data)
    df = df[['id', 'title', 'price', 'category']]
    df.columns = ['product_id', 'product_name', 'price', 'category']
    return df