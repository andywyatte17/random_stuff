cmake_minimum_required(VERSION 3.0.2)

# https://cognitivewaves.wordpress.com/cmake-and-visual-studio/

set (LIBNAME {{ libname }})

project(${LIBNAME})

{% for source in sources -%}
set({{ source.name }}
{% for file in source.files %}  "{{ file }}"{% if not loop.last%},{% endif %}
{% endfor -%}
)
{% endfor -%}