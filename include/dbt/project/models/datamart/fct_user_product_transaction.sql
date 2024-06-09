with base as (
    select
        t.receipt_id,
        u.user_id,
        u.name,
        u.product_id,
        pi.product_name,
        pi.tag_name,
        t.quantity,
        t.total_price
    from 
        {{ ref('int_user_behaviour') }} u
    left join
        {{ ref('int_transaction_information') }} t
    on u.user_id = t.user_id 
    left join
        {{ ref('int_product_information')}} pi
    on u.product_id = pi.product_id
)

select * from base 
order by receipt_id asc