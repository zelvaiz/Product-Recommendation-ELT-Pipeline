with base as (
    select * from {{ ref('int_product_information') }}
)

select * from base