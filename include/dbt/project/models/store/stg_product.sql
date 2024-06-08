WITH source AS (
    SELECT
        CAST(product_id AS INTEGER) AS product_id,
        product_name,
        price,
    FROM {{ source('capstone_data', 'product')}}
    WHERE product_id IS NOT NULL
)
SELECT
    product_id,
    product_name,
    price,
FROM source
