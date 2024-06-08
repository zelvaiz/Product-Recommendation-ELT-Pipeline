with source as (
    SELECT
        CAST(country_id as INTEGER) as country_id,
        country_name

    FROM {{source('capstone_data', 'country')}}
    WHERE country_id is not null 
)

SELECT * FROM source