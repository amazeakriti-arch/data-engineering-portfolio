# Week 6 – AWS Glue Parquet ETL Project

## 📌 Overview
This project demonstrates a cloud ETL pipeline using AWS Glue to convert CSV data into Parquet format and query it using Amazon Athena.

---

## 🏗 Architecture
S3 (CSV) → AWS Glue → S3 (Parquet) → Athena

---

## 🔄 ETL Flow
- Extract: Read CSV from S3
- Transform: Schema mapping via Glue
- Load: Write data in Parquet format

---

## 🛠 AWS Services Used
- Amazon S3
- AWS Glue (Crawler & Job)
- AWS Athena
- IAM

---

## 🚀 How to Run
1. Upload CSV file to S3 `raw/`
2. Run Glue crawler
3. Run Glue ETL job
4. Query Parquet data using Athena

---

## 🎯 Learning Outcomes
- Parquet format benefits
- Glue crawler schema inference
- Serverless ETL
- Athena SQL on S3
