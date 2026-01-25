# AWS Glue Workflow Steps

1. Workflow starts manually or on schedule
2. Raw CSV crawler runs and updates Glue Catalog
3. Trigger waits for crawler completion
4. ETL job runs only after crawler succeeds
5. Parquet data is written to curated S3 path
6. Workflow completes successfully
