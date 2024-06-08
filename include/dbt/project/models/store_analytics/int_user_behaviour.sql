with source as (
    select 
        c.user_id,
        c.product_id,
        c.view_duration,
        c.cart_time_days,
        c.read_review,
)