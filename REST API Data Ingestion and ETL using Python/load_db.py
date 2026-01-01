from sqlalchemy import Float, Integer, String
from sqlalchemy.dialects import oracle
from config import ENGINE

def load_to_db(df):
    dtype_mapping = {
        "product_id": Integer(),
        "product_name": String(255),
        "price": Float().with_variant(
            oracle.FLOAT(binary_precision=126), "oracle"
        ),
        "category": String(100)
    }

    with ENGINE.begin() as conn:  # auto-commit
        df.to_sql(
            name="products",
            con=conn,
            if_exists="replace",
            index=False,
            dtype=dtype_mapping
        )
