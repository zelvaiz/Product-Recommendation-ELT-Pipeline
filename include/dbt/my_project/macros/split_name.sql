{% macro split_name(column_name) %}
    SELECT
        CASE
            WHEN strpos({{ column_name }}, ' ') > 0 THEN substr({{ column_name }}, 1, strpos({{ column_name }}, ' ') - 1)
            ELSE {{ column_name }}
        END AS first_name,
        CASE
            WHEN strpos({{ column_name }}, ' ') > 0 THEN substr({{ column_name }}, strpos({{ column_name }}, ' ') + 1)
            ELSE NULL
        END AS last_name
{% endmacro %}