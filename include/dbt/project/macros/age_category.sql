{% macro age_category(column_name) %}
    case
        when {{column_name}} >= 30 then 'Adult'
        when {{column_name}} >= 20 then 'Young Adult'
        when {{column_name}} >= 13 then 'Teen'
        when {{column_name}} >= 5 then 'Kid'
        when {{column_name}} >= 0 then 'Baby'
    end
{% endmacro %}