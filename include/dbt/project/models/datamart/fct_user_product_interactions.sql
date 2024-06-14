with base as (
    select
        u.user_id,
        u.product_id,
        u.view_duration,
        u.cart_time_days,
        u.read_review,
        pi.product_name, -- hapus masukkan ke dim_product
        pi.price, -- hapus masukkan ke dim_product
        pi.rating, -- hapus masukkan ke dim_product
        pi.rating_name, -- hapus masukkan ke dim_product
        pi.tag_name --hapus masukkan ke dim_product
    from 
        {{ ref('int_user_behaviour') }} u
    left join
        {{ ref('int_product_information')}} pi
    on u.product_id = pi.product_id
)

select * from base 