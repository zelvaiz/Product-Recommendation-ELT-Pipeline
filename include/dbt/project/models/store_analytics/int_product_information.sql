with source as (
    select
        p.product_id,
        p.product_name,
        p.price,
        r.rating,
        t.tag_name
from 
    {{ref('stg_product')}} p
left join
    {{ref('stg_review')}} r
on p.product_id = r.product_id
left join
    {{ref('stg_tags')}} t
on p.tag_id = t.tag_id
)

select * from source