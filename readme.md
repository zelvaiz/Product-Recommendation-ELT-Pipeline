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

## Make Bucket in Google Cloud Service (CSV Files)
- Open Google Cloud Service
- Input Bucket in search text box 
- Create new Bucket 
![bucket](https://github.com/ahmadalpadani/Project-Capstone/blob/main/assets/Bucket.png) 
- Upload CSV file to the Bucket folder
![bucket_folder](https://github.com/ahmadalpadani/Project-Capstone/blob/main/assets/bucket_folder.jpg) 
- Setting CSV Bucket file to the public 

## Data Ingestion With Airbyte

### Setup Connection for Airbyte
Open url http://localhost:8000 for Airbyte UI
- User: `airflow`
- Password: `airflow`
Click New Connection

### Data Source From CSV
- In Define source, choose setup new source
- Input csv in search text box then click File
- Input dataset name and choose file format csv 
- For Storage Provider choose HTTPS : Public Web and input URL : 
https://storage.googleapis.com/project_capstone_alterra_2/product%20(1).csv (Product) 
https://storage.googleapis.com/project_capstone_alterra_2/cart.csv (Cart) 
https://storage.googleapis.com/project_capstone_alterra_2/country.csv (Country)
https://storage.googleapis.com/project_capstone_alterra_2/gender.csv (Gender) 
https://storage.googleapis.com/project_capstone_alterra_2/purchased.csv (Purchased)
https://storage.googleapis.com/project_capstone_alterra_2/review.csv (Review) 
https://storage.googleapis.com/project_capstone_alterra_2/tags%20(1).csv (Tags)
- Click set up source 

### Data Source From Postgres
- In Define source, choose setup new source
- Input postgres in search text box then click File
- Fill:
```bash
Host : localhost
Port : 5441
Database_Name : mudb
Username: postgres
Password : admin
```
![postgres](https://github.com/ahmadalpadani/Project-Capstone/blob/main/assets/postgres.jpg) 
- Click set up source 

### Define destination connection in Airbyte (To Bigquery)
- In Define destination, choose setup new destination
- Input Bigquery in search text box
- Fill the colum for Bigquery Connnection, please refer to this article [Airflow_Bigquery](https://docs.airbyte.com/integrations/destinations/bigquery?_gl=1*106oqw*_gcl_au*MjEwNjIyMzgwMi4xNzE3NTc2NjY0)
![airflow_bigquery](https://github.com/ahmadalpadani/Project-Capstone/blob/main/assets/bigquery.jpg) 
- Click Setup destination

### Configure connection in Airbyte
- In Connection, input connection name
- In Configuration, Choose schedule type manual(because airbyte job will trigger by airflow)
- Click Setup connection
- Click Sync Now

## Data Modelling With DBT

### Setup venv and install DBT

Move to directory include and make new directory
```bash
cd include
mkdir dbt
```

Setup venv and install dbt-bigquery
```bash
python -m venv .venv
source .venv/bin/activate
pip install dbt-bigquery # Note: DBT has many DBMS adapter
```

### Create requirements.txt

In order to keep track what packages you have installed, it is better to make an up-to-date list of `requirements.txt`.

You can list your dbt-related packages by invoking and Put the list into `requirements.txt`.


```bash
pip freeze | grep dbt >> requirement.txt
```

The output will be similar to:

```
dbt-core==1.6.3
dbt-extractor==0.4.1
dbt-postgres==1.6.3
dbt-semantic-interfaces==0.2.0
```

If you need to install other packages, you should add them into `requirements.txt` as well

Next time you want to install `dbt`, you can simply run `pip install -r requirements.txt`

### Setup DBT project

```bash
dbt init project
```

### Setup DBT Profile

Move to directory project and make a new file, name 'profiles.yml'

```bash
cd project
touch profiles.yml
```

You can set your `profiles.yml` as follow:

```yml
project:
  outputs:
    dev:
      dataset: Project_Capstone
      job_execution_timeout_seconds: 300
      job_retries: 1
      keyfile: latihan-cloud-alterra-82d3d61abdd0.json
      location: US
      method: service-account
      priority: interactive
      project: latihan-cloud-alterra
      threads: 1
      type: bigquery
  target: dev
```
Note: Please fill in according to your respective bigquery information

### Setup DBT Project configuration

To setup DBT project configuration, you can edit `project/dbt_project.yml`.

Make sure your `models` looks like this:

```yml
models:
  project:
    # Config indicated by + and applies to all files under models/example/
    store:
      +materialized: table
    store_analytics:
      +materialized: table
    datamart:
      +materialized: table
```

### Defining Source

To define source, you can put the following YAML into `models/store/source.yml`

```yml
version: 2 
sources:
  - name: capstone_data
    schema: Project_Capstone
    tables: 
      - name: user
      - name: product
      - name: purchased
      - name: cart
      - name: country
      - name: gender
      - name: tags
      - name: review
      - name: product2
      - name: tags2
```

### Creating a Model

We make 3 model directory under `models/store`, `models/store_analytics`, `models/data_mart`

We will define as much as models as we need, but in this example, we only create a single model named `stg_user`.

You can then define a `stg_user.sql` under the directory `models/store`:

```sql
WITH source AS (
    SELECT 
        CAST(user_id AS INTEGER) AS user_id,
        name,
        age,
        {{age_category('age')}} as age_category,
        email,
        CAST(gender_id AS INTEGER) AS gender_id,
        CAST(country_id AS INTEGER) AS country_id
    FROM {{ source('capstone_data', 'user') }}
    WHERE user_id IS NOT NULL
)

SELECT * FROM source
```
For more information about models, you can refer to the following link [Models](https://github.com/ahmadalpadani/Project-Capstone/tree/main/include/dbt/project/models)


### Installing dbt package

You can install additional dbt package by modifying `packages.yml` and invoking `dbt deps` afterwise.

Make file `packages.yml` uder directory `dbt/project`

Put the dbt utils packages to `packages.yml`
```yml
packages:
  - package: dbt-labs/dbt_utils
    version: 1.2.0
```

Invoking `dbt deps`
```bash
dbt deps
```
See dbt documentation for more information: https://docs.getdbt.com/docs/build/packages

### Add test

You can add test to your model by modifying your `schema.yml`

In this example, we will make test for intermediate directory (`models/store_analytics`) from dbt utils by modifying  `int_schema.yml`

```yml
version: 2

models:
  - name: int_transaction_information
    description: "transaction information intermediate area "
    tests:
      - dbt_utils.unique_combination_of_columns:
          combination_of_columns:
            - receipt_id
            - product_name
```

To see what kind of test you can pefrom, you can visit dbt_utils documentation: https://github.com/dbt-labs/dbt-utils

### Creating a Macro

Macro allows you to put reusable logic in one place.

To setup DBT project configuration, you can edit `project/macros`.

For example, we want to create an age category by adding a category according to the age of the customer (for example, if the age of the customer is between 13 to 19 years old, it is categorized as a teenager).

In this case, you can create a file under the `macros` folder (for example, `macros/age_category.sql`)

```sql
{% macro age_category(column_name) %}
    case
        when {{column_name}} >= 30 then 'Adult'
        when {{column_name}} >= 20 then 'Young Adult'
        when {{column_name}} >= 13 then 'Teen'
        when {{column_name}} >= 5 then 'Kid'
        when {{column_name}} >= 0 then 'Baby'
    end
{% endmacro %}
```

Once you define the macro, you can call the macro in your model definition, in this case in `stg_user`

```sql
WITH source AS (
    SELECT 
        CAST(user_id AS INTEGER) AS user_id,
        name,
        age,
        {{age_category('age')}} as age_category,
        email,
        CAST(gender_id AS INTEGER) AS gender_id,
        CAST(country_id AS INTEGER) AS country_id
    FROM {{ source('capstone_data', 'user') }}
    WHERE user_id IS NOT NULL
)

SELECT * FROM source
```
For more information about models, you can refer to the following link [Macros](https://github.com/ahmadalpadani/Project-Capstone/tree/main/include/dbt/project/macros)


## Create Airflow Dags for Trigger Airbyte and DBT Jobs

Open url http://localhost:8000 for Airbyte UI
- User: `airflow`
- Password: `airflow`


