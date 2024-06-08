with source as (
    select
        t.tag_name, 
        count(p.tag_id) as total_tag
    from {{ref('stg_tags')}} t
    left join {{ref('stg_product')}} p
    on t.tag_id = p.tag_id
    group by t.tag_name
    order by total_tag desc 
)

select * from source
order by total_tag desc 
