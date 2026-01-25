# Week 7 – AWS Glue Orchestrated ETL Workflow

## Objective
Build a production-style ETL orchestration using AWS Glue Workflows to automate:
- Raw data ingestion
- ETL execution
- Dependency-based execution

## Architecture
- Raw CSV files stored in Amazon S3
- AWS Glue Crawler catalogs raw data
- AWS Glue ETL Job transforms CSV → Parquet
- AWS Glue Workflow orchestrates execution order

## Workflow Sequence
1. Start Workflow
2. Run Raw Data Crawler
3. Trigger ETL Job on crawler completion
4. Write curated Parquet data to S3

## Technologies Used
- AWS Glue
- AWS Glue Workflows
- AWS Glue Crawlers
- PySpark (DynamicFrames)
- Amazon S3
- AWS Glue Data Catalog

## Outcome
- Fully automated ETL pipeline
- No manual intervention required
- Production-ready orchestration design
