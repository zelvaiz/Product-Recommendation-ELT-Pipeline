with source as (
    SELECT
        CAST(product_id as INTEGER) as product_id,
        review_score as rating,
        {{review_rate('review_score')}} as rating_name

    FROM {{source('capstone_data', 'review')}}
    WHERE product_id is not null 
)

SELECT * FROM source