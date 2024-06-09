with base as (
    select 
        pi.product_id,
        pi.product_name,
        pi.price,
        pi.rating,
        pi.tag_name
    from {{ ref('int_product_information') }} pi
)

select * from base