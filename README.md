# ETL Pipeline for Bank Marketing Campaign Data | End-to-End-Project

## Overview
This project demonstrates a fully functional ETL pipeline that extracts, transforms (including sanitization of data using the Pandas library), loads, and analyzes data. The pipeline leverages Google Cloud Platform (GCP) services such as Cloud Storage and BigQuery.

## Objective
Tasked with cleaning and reformatting marketing campaign data on personal loans to meet specified structure and data types for BigQuery, enabling storage and seamless integration of future campaigns. The bank has supplied a CSV file, `bank_marketing.csv`, which needs to be processed, sanitized using the Pandas library, and split into three final CSV files for further analysis.

## Tools
`Google Cloud Storage` : A scalable, secure cloud storage service from Google that allows users to store and retrieve large amounts of data. It is often used for data backup, archival, and serving content.

`Google BigQuery` : A fully managed, serverless data warehouse service by Google, designed for running fast SQL queries on large datasets. It is ideal for analyzing big data and building data analytics applications.

`Jupyter Notebook`: An open-source web application that allows users to create and share documents containing live code, equations, visualizations, and narrative text. It is widely used in data science and machine learning for interactive analysis and exploration.

`Pandas` : A powerful Python library for data manipulation and analysis. It provides data structures like DataFrame, which are used for working with structured data, making tasks like cleaning, transforming, and analyzing data much easier.

## Pipeline Architecture

![bmd](https://github.com/user-attachments/assets/c931eb59-ee49-456b-b568-d5973579d752)

### 1. Data Extraction
Upload the raw data file : `bank_marketing.csv` to a designated Google Cloud Storage bucket for centralized access.
### 2. Data Transformation
Transforming raw data using Jupyter Notebook and the Pandas library on Google Cloud Storage to clean, reformat, and split the data into t3 final CSV files: 
1. `campaigns.csv`
2. `client.csv`
3. `economics.csv.`
### 3. Final Data Repository
Leverage Google Cloud Storage to securely store the cleaned data, ensuring it is readily available for future use in data analysis. This stored data can then be easily integrated with Google BigQuery, allowing for efficient querying and in-depth analysis to gain valuable insights and make data-driven decisions.
### 4. Data Warehouse & Analytics
Leverage  Google BigQuery for efficient querying and analysis to gain insights for data-driven decisions. The cleaned data is formatted according to the bank's requirements, making it ready for future marketing campaigns."





