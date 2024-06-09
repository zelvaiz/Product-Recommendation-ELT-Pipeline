with source as (
    select 
        c.user_id,
        u.name,
        c.product_id,
        p.product_name,
        c.view_duration,
        c.cart_time_days,
        c.read_review
    from 
        {{ref('stg_cart')}} c
    left join
        {{ref('stg_user')}} u 
    on c.user_id = u.user_id
    left join
        {{ref('stg_product')}} p
    on c.product_id = p.product_id
)

select * from source