with base as (
    select
        u.user_id,
        u.product_id,
        u.view_duration,
        u.cart_time_days,
        u.read_review,
        pi.product_name,
        pi.price,
        pi.rating,
        pi.rating_name,
        pi.tag_name
    from 
        {{ ref('int_user_behaviour') }} u
    left join
        {{ ref('int_product_information')}} pi
    on u.product_id = pi.product_id
)

select * from base 