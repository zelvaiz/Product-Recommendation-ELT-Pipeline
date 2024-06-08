WITH source AS (
    SELECT
        CAST(product_id AS INTEGER) AS product_id,
        product_name,
        CAST(tag_id AS INTEGER) AS tag_id,
        price,
    FROM {{ source('capstone_data', 'product2')}}
    WHERE product_id IS NOT NULL and tag_id is not null
)
SELECT * FROM source
