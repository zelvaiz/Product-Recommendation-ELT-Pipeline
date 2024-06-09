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
