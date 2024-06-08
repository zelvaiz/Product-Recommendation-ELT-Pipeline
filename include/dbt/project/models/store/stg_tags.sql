with source as (
    SELECT
        CAST(tag_id as INTEGER) as tag_id,
        tag_name

    FROM {{source('capstone_data', 'tags')}}
    WHERE tag_id is not null 
)

SELECT * FROM source