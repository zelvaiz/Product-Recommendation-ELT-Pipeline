with source as (
    SELECT
        CAST(user_id as INTEGER) as user_id,
        CAST(product_id as INTEGER) as product_id,
        page_view as view_duration,
        CAST(cart_time_days/1440 as integer) as cart_time_days,
        read_review

    FROM {{source('capstone_data', 'cart')}}
    WHERE product_id is not null and user_id is not null
)

SELECT * FROM source