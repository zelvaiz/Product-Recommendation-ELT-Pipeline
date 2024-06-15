with base as (
    select
        user_id,
        product_id,
        view_duration,
        cart_time_days,
        read_review,
    from 
        {{ ref('int_user_behaviour') }}
)

select * from base 