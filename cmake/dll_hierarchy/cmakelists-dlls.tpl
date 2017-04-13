cmake_minimum_required(VERSION 3.0.2)

set (LIBNAME {{ libname }})

project(${LIBNAME})

macro(install_libs)
  FILE(TO_CMAKE_PATH "${CMAKE_CURRENT_BINARY_DIR}/install/" INSTALL_DST_DIR_TMP)
  if(CMAKE_CL_64)
    INSTALL(TARGETS ${LIBNAME}
      ARCHIVE DESTINATION "${INSTALL_DST_DIR_TMP}/libs"
      CONFIGURATIONS Debug;Release;RelWithDebInfo;MinSizeRel)
  else()
    INSTALL(TARGETS ${LIBNAME}
      ARCHIVE DESTINATION "${INSTALL_DST_DIR_TMP}/libs"
      CONFIGURATIONS Debug;Release;RelWithDebInfo;MinSizeRel)
  endif()
endmacro()

{% for source in sources -%}
set({{ source.name }}
{% for file in source.files %}  "{{ file }}"
{% endfor -%}
)

{% endfor -%}

{% for source in sources -%}
source_group("{{ source.group }}" FILES ${{ '{' }}{{ source.name }}{{ '}' }})

{% endfor %}

add_library(${LIBNAME} {{ shared_static }}
{% for source in sources -%}
${{ '{' }}{{ source.name }}{{ '}' }}
{% endfor -%}
)

# INSTALL_DST_ROOT should be in CMAKE_PATH format - it then works correctly
#   with INSTALL(CODE "...")
FILE(TO_CMAKE_PATH "${CMAKE_CURRENT_BINARY_DIR}/install/" INSTALL_DST_ROOT)
SET(INSTALL_DST_ROOT "${INSTALL_DST_ROOT}/HeaderFiles/Dlls/${LIBBASE}")

# Clean-up header files folder
# install(CODE "FILE(REMOVE_RECURSE ${INSTALL_DST_ROOT})")

# Install header files
{% for inst_f in install_files %}
INSTALL(FILES
  {% for file in inst_f.files %} "{{ file }}" {% endfor -%}
  DESTINATION "${INSTALL_DST_ROOT}/{{ inst_f.folder }}")

{% endfor -%}

# Give the output name something different to the Release
set_target_properties(${LIBNAME} PROPERTIES OUTPUT_NAME_DEBUG ${LIBNAME}D)
set_target_properties(${LIBNAME} PROPERTIES COMPILE_PDB_NAME_DEBUG ${LIBNAME}D)
set_target_properties(${LIBNAME} PROPERTIES COMPILE_PDB_NAME_RELEASE ${LIBNAME})
set_target_properties(${LIBNAME} PROPERTIES COMPILE_PDB_NAME_RELWITHDEBINFO ${LIBNAME})
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAG} /EHsc /wd4456 /wd4458 /wd4459 /wd4457")

install_libs()
