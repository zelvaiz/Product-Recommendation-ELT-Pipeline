with base as (
    select * from {{ ref('int_transaction_information') }}
)

select * from base