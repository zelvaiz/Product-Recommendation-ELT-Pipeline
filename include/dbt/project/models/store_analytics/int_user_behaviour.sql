with source as (
    select 
        user_id,
        product_id,
        view_duration,
        cart_time_days,
        read_review
    from {{ref('stg_cart')}}
)

select * from source