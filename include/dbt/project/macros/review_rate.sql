{% macro review_rate(column_name) %}
    case
        when {{column_name}} >= 4 then 'Excellent'
        when {{column_name}} >= 3 then 'Very Good'
        when {{column_name}} >= 2 then 'Good'
        when {{column_name}} >= 1 then 'Bad'
        when {{column_name}} >= 0 then 'Very Bad'
    end
{% endmacro %}