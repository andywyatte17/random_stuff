# Set the '_varResult' variable to be equal to the like of variables like
#   SOURCES_..._PH - this returns to _varResult the result like
#   SOURCES_A_PH;SOURCES_A_SUB_PH
#
function (getVariablesLike_SOURCES_XYZ_PH _varResult)
  set(_prefix "SOURCES_")
  get_cmake_property(_vars VARIABLES)
  string (REGEX MATCHALL "(^|;)${_prefix}[A-Za-z0-9_]*_PH" _matchedVars "${_vars}")
  set (${_varResult} ${_matchedVars} PARENT_SCOPE)
endfunction()

function (install_sources_xyz_ph_files HEADER_PREFIX)
  getVariablesLike_SOURCES_XYZ_PH(VARS_SOURCES_PH)
  foreach (_SOURCE_PH_VAR_NAME ${VARS_SOURCES_PH})
    set(_SOURCE_PH_FILENAME_LIST "${${_SOURCE_PH_VAR_NAME}}")
    foreach(_SOURCE_PH_FILE ${_SOURCE_PH_FILENAME_LIST})
      get_filename_component(_SOURCE_PH_DEST_DIR ${_SOURCE_PH_FILE} DIRECTORY)
      INSTALL(FILES "${_SOURCE_PH_FILE}" DESTINATION "${HEADER_PREFIX}/${_SOURCE_PH_DEST_DIR}")
    endforeach()
  endforeach()
endfunction()
