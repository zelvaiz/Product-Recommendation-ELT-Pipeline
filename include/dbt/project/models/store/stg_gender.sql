with source as (
    SELECT
        CAST(gender_id as INTEGER) as gender_id,
        gender_name,

    FROM {{source('capstone_data', 'gender')}}
    WHERE gender_id is not null
)

SELECT * FROM source