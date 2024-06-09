with base as (
    select * from {{ ref('int_user_information') }}
)

select * from base