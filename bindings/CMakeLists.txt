# QuickEd library C++ binding
add_library(quickedcpp STATIC cpp/quicked.cpp)
target_include_directories(quickedcpp PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/cpp)
target_link_libraries(quickedcpp PRIVATE quicked)

# QuickEd library Python binding (based on C++ binding)
find_package(Python3 REQUIRED COMPONENTS Interpreter Development.Module)
add_subdirectory(python/pybind11)

pybind11_add_module(pyquicked python/quicked.cpp cpp/quicked.cpp)
set_target_properties(pyquicked PROPERTIES OUTPUT_NAME quicked ARCHIVE_OUTPUT_NAME pyquicked)
target_include_directories(pyquicked PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/cpp)
target_link_libraries(pyquicked PRIVATE quicked)
if (NOT MSVC)
    target_compile_options(pyquicked PRIVATE -fvisibility=hidden)
endif()

install(TARGETS pyquicked DESTINATION . COMPONENT pyquicked EXCLUDE_FROM_ALL)
install(FILES python/quicked.pyi DESTINATION . COMPONENT pyquicked EXCLUDE_FROM_ALL)