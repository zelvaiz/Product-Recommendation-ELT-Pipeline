{% macro age_category(column_name) %}
    case
        when {{column_name}} >= 40 then 'Old Adults'
        when {{column_name}} >= 30 then 'Middle-aged Adults'
        when {{column_name}} >= 20 then 'Young Adult'
        when {{column_name}} >= 13 then 'Teen'
    end
{% endmacro %}