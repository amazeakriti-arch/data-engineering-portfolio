## Project Overview
This project demonstrates an end-to-end REST API data ingestion and ETL pipeline.
Data is extracted from a REST API, transformed using Pandas, stored as CSV (data lake layer),
and loaded into an Oracle database using SQLAlchemy.

### Features
- REST API ingestion
- JSON data transformation
- Load to CSV (data lake layer)
- Load to Database using SQLAlchemy
- Modular ETL design

### Tech Stack
- Python
- Pandas
- REST APIs
- SQLAlchemy
- Oracle (DB)
Oracle connectivity implemented using SQLAlchemy with python-oracledb (thin mode).

## How to Run
1. Run the pipeline:
   python main.py

   ## Data Flow
REST API → JSON → Pandas Transformation → CSV → Oracle Database
