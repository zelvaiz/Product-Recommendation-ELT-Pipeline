with source as (
    select
        u.user_id,
        u.name,
        u.email,
        u.age,
        u.age_category,
        g.gender_name as gender,
        c.country_name as country
    FROM
        {{ref('stg_user')}} u
    left join
        {{ref('stg_gender')}} g
    on u.gender_id = g.gender_id
    left join
        {{ref('stg_country')}} c
    on u.country_id = c.country_id
)

select *  from source