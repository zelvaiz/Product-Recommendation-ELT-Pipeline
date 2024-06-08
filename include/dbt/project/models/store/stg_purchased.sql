with source as (
    SELECT
        CAST(purchased_id as INTEGER) as purchased_id,
        CAST(product_id as INTEGER) as product_id,
        CAST(user_id as INTEGER) as user_id,
        qty as quantity,
    FROM {{source('capstone_data', 'purchased')}}
    WHERE purchased_id is not null and product_id is not null and user_id is not null
)

SELECT * FROM source