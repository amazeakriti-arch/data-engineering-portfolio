# AWS Lambda S3 Text ETL (Week 5)

## 📌 Overview
This project demonstrates an event-driven ETL pipeline using AWS Lambda and Amazon S3.
When a text file is uploaded to an S3 bucket, a Lambda function is automatically triggered
to transform the data and store the output back in S3.

---

## 🏗️ Architecture
S3 (Input) → Lambda (ETL) → S3 (Output)

---

## ⚙️ Technologies Used
- AWS Lambda (Python 3.10)
- Amazon S3
- IAM
- Boto3
- AWS CLI

---

## 🔄 ETL Flow
1. Upload a text file to `input/` folder in S3
2. S3 event triggers Lambda
3. Lambda reads file content
4. Content is reversed (string transformation)
5. Output is written to `output/output.txt`

---

## 🧪 Example

### Input
