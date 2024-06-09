with source as (
    select
        pu.purchased_id as receipt_id,
        u.user_id,
        u.name,
        p.product_id,
        p.product_name,
        t.tag_name,
        p.price,
        pu.quantity,
        round(p.price*pu.quantity, 2) as total_price
    from
        {{ref('stg_purchased')}} pu
    left join
        {{ref('stg_product')}} p
    on pu.product_id = p.product_id
    left join
        {{ref('stg_user')}} u
    on pu.user_id = u.user_id
    left join 
        {{ref('stg_tags')}} t
    on p.tag_id = t.tag_id
)

select * from source