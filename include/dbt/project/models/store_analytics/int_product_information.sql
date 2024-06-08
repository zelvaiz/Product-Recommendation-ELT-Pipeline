with source as (
    select
        p.product_id,
        p.product_name,
        p.price,
        r.rating
from 
    {{ref('stg_product')}} p
left join
    {{ref('stg_review')}} r
on p.product_id = r.product_id
)

select * from source