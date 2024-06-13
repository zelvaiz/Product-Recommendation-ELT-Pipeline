# Product Reccomendation ELT Pipeline: Extract With Airbyte, Load to Bigquery, Transform With DBT and Orchestration With Airflow

## User Case

TechGear adalah perusahaan yang menjual berbagai macam perangkat elektronik. Dalam proses bisnisnya, TechGear menggunakan website sebagai instrumen jual beli utama, website tersebut menampung berbagai macam data hasil jual beli seperti: user activity data, product transaction data, dan user behavior data.

Untuk menunjang peningkatan bisnis perusahaan TechGear, perusahaan berusaha mengembangkan sistem Product Recommendation untuk mengetahui kecocokan setiap produk dengan masing-masing pelanggan berdasarkan analisa data user behavior (cth: product views, cart additions).

## Project Goals

1. Data Ingestion - Membuat pipeline data ingestion untuk mengekstrak raw data ke dalam GCP BigQuery.
2. Data Transformation - Menggunakan DBT untuk melakukan pemodelan data dan mengubah data ke dalam star schema.
3. Data Orchestration - Menggunakan Airflow untuk melakukan otomatisasi terhadap pipeline yang telah dibetuk.
4. Data Reporting/Analytics - Menggunakan Looker Studio untuk membuat dashboard untuk tujuan pelaporan atau analisis.

## ELT Data Architecture 

![data_architecture](https://github.com/ahmadalpadani/Project-Capstone/blob/main/assets/ELT%20Archicteture.png) 

## Start Docker Compose
- git clone this code to local
- run docker compose
  ```
  docker compose up -d
  ``` 

## Make Bukcet in Google Cloud Service (CSV Files)
- Open Google Cloud Service
- Input Bucket in search text box 
- Create new Bucket 
![bucket](https://github.com/ahmadalpadani/Project-Capstone/blob/main/assets/Bucket.png) 

- Upload CSV file to the Bucket folder
![bucket_folder](https://github.com/ahmadalpadani/Project-Capstone/blob/main/assets/bucket_folder.jpg) 

- Setting CSV Bucket file to the public 

