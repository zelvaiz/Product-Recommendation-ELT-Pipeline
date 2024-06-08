with source as (
    select
        pu.purchased_id as receipt_id,
        u.name,
        p.product_name,
        p.price,
        pu.quantity,
        (p.price*pu.quantity) as total_price
    from
        {{ref('stg_purchased')}} pu
    left join
        {{ref('stg_product')}} p
    on pu.product_id = p.product_id
    left join
        {{ref('stg_user')}} u
    on pu.user_id = u.user_id
)

select * from source