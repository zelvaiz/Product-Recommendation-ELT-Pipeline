with source as (
    select
        tag_name, 
        count(tag_name) as total_tag
    from {{ref('int_product_information')}} 
    group by tag_name
    order by total_tag desc 
)

select * from source
order by total_tag desc 
