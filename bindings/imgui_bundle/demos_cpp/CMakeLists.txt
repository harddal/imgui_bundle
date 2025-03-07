set(CMAKE_CXX_STANDARD 20)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/bin")
include_directories(.)

set(demos_cpp_folder ${CMAKE_CURRENT_LIST_DIR})


function(add_demo_cpp)
    # Creates an app using imgui_bundle_add_app, and link it with demo_utils
    # Usage:
    #     add_demo_cpp(demo_name demo_file_1.cpp demo_file_2.cpp)
    set(args ${ARGN})
    list(GET args 0 demo_name)
    set(demos_asset_folder ${IMGUIBUNDLE_PATH}/bindings/imgui_bundle/demos_assets)
    imgui_bundle_add_app(${args} ASSETS_LOCATION ${demos_asset_folder})
    if(MSVC)
        hello_imgui_msvc_target_set_folder(${demo_name} demos_cpp)
    endif()
    target_link_libraries(${demo_name} PUBLIC demo_utils)
    if (EMSCRIPTEN)
        # Bundle demos_assets
        hello_imgui_bundle_assets_from_folder(${demo_name} ${demos_cpp_folder}/../demos_assets)
    endif()
endfunction()

function(add_single_file_demo_cpp demo_cpp_file)
    # Creates a demo app
    # Usage:
    #     add_single_file_demo_cpp(demo_file.cpp)
    get_filename_component(demo_name "${demo_cpp_file}" NAME_WE)
    add_demo_cpp(${demo_name} ${demo_cpp_file})
endfunction()

function(add_auto_demo demo_cpp_file)
    # Creates a demo app, and provides main() automatically
    # Usage:
    #     add_auto_demo(demo_file.cpp)
    # (demo_file.cpp should provide a function named according to the containing file, e.g. `void demo_file()`)
    get_filename_component(demo_cpp_file "${demo_cpp_file}" NAME)
    get_filename_component(demo_name "${demo_cpp_file}" NAME_WE)
    add_demo_cpp(${demo_name} ${demo_cpp_file})

    # Read the contents of the cpp file
    file(READ "${demo_cpp_file}" demo_cpp_file_content)

    # If the cpp file does not contain a main function, provide it
    if (NOT "${demo_cpp_file_content}" MATCHES "int main")
        message(STATUS "${demo_cpp_file} does not contain a main function, adding it!")
        set(main_file ${CMAKE_CURRENT_BINARY_DIR}/${demo_cpp_file}.autogenerated.cpp)
        configure_file(${demos_cpp_folder}/_auto_main/_auto_main.cpp.in ${main_file})
        target_sources(${demo_name} PRIVATE ${main_file})
    endif()

endfunction()

function(add_this_folder_demos)
    # Creates demo apps for all cpp files in the current folder
    FILE(GLOB demo_cpp_files *.cpp)
    FOREACH(demo_cpp_file ${demo_cpp_files})
        add_single_file_demo_cpp(${demo_cpp_file})
    ENDFOREACH()
endfunction()

function(add_this_folder_auto_demos)
    # Creates demo apps for all cpp files in the current folder, and provide a main for them
    FILE(GLOB demo_cpp_files *.cpp)
    FOREACH(demo_cpp_file ${demo_cpp_files})
        add_auto_demo(${demo_cpp_file})
    ENDFOREACH()
endfunction()


function(add_this_folder_as_demos_library)
    file(GLOB sources *.cpp)
    get_filename_component(folder_name "${CMAKE_CURRENT_LIST_DIR}" NAME_WE)
    set(demos_library_name ${folder_name})
    add_library(${demos_library_name} ${sources})
    target_link_libraries(${demos_library_name} imgui_bundle)
    target_compile_definitions(${demos_library_name} PRIVATE IMGUI_BUNDLE_BUILD_DEMO_AS_LIBRARY)
endfunction()


add_subdirectory(demo_utils)
add_subdirectory(demos_immapp)
add_subdirectory(demos_node_editor)
add_subdirectory(demos_imguizmo)
add_subdirectory(demos_tex_inspect)
add_subdirectory(sandbox)
if (IMGUI_BUNDLE_WITH_IMMVISION)
    add_subdirectory(demos_immvision)
endif()

add_this_folder_auto_demos()
add_this_folder_as_demos_library()

if (EMSCRIPTEN)
    set(demos_python_folder ${demos_cpp_folder}/../demos_python)

    set(imgui_demo_src_folder ${IMGUIBUNDLE_PATH}/external/imgui/imgui/)
    set(imgui_demo_tmp_folder ${CMAKE_CURRENT_BINARY_DIR}/tmp/imgui_demo_code)
    file(COPY ${imgui_demo_src_folder}/imgui_demo.cpp DESTINATION ${imgui_demo_tmp_folder})
    file(COPY ${imgui_demo_src_folder}/imgui_demo.py DESTINATION ${imgui_demo_tmp_folder})

    target_link_options(demo_imgui_bundle PRIVATE "SHELL:--preload-file ${demos_cpp_folder}@/demos_cpp")
    target_link_options(demo_imgui_bundle PRIVATE "SHELL:--preload-file ${demos_python_folder}@/demos_python")
    target_link_options(demo_imgui_bundle PRIVATE "SHELL:--preload-file ${imgui_demo_tmp_folder}@code/imgui")
    set(python_backends_folder ${CMAKE_CURRENT_LIST_DIR}/../python_backends)
    target_link_options(demo_imgui_bundle PRIVATE "SHELL:--preload-file ${python_backends_folder}@/python_backends")
endif()


target_link_libraries(demo_imguizmo_launcher PRIVATE demos_imguizmo)
target_link_libraries(demo_node_editor_launcher PRIVATE demos_node_editor)
target_link_libraries(demo_tex_inspect_launcher PRIVATE demos_tex_inspect)
target_link_libraries(demo_imgui_bundle PRIVATE
    demos_cpp
    demos_imguizmo
    demos_tex_inspect
    demos_node_editor
    demo_utils
)
if (IMGUI_BUNDLE_WITH_IMMVISION)
    target_link_libraries(demo_immvision_launcher PRIVATE demos_immvision)
    target_link_libraries(demo_imgui_bundle PRIVATE demos_immvision)
endif()

FILE(COPY ../demos_assets DESTINATION ${CMAKE_RUNTIME_OUTPUT_DIRECTORY})

if (MSVC)
    FILE(COPY msvc_note.txt DESTINATION ${CMAKE_RUNTIME_OUTPUT_DIRECTORY})
endif()

if(EMSCRIPTEN AND HELLOIMGUI_EMSCRIPTEN_PTHREAD)
    # Needed addition for multithread support (required by ImGui Test Engine)
    # Note: see the shell.emscripten.html in this folder we are using a custom shell,
    #       that provides Cross-origin isolation (COOP and COEP) through a service worker
    #       for situations in which you can't control the headers (e.g. GitHub pages).
    #
    # coi-serviceworker.js was found at https://github.com/gzuidhof/coi-serviceworker, and manually patched:
    #    see https://github.com/gzuidhof/coi-serviceworker/issues/20
    #    and https://github.com/gzuidhof/coi-serviceworker/compare/master...tamo:coi-serviceworker:coep-ua-brand
    #
    # coi-serviceworker.js provides Cross-origin isolation (COOP and COEP) through a service worker
    # for situations in which you can't control the headers (e.g. GitHub pages).

    get_property(runtime_output_directory TARGET demo_imgui_bundle PROPERTY RUNTIME_OUTPUT_DIRECTORY)
    FILE(MAKE_DIRECTORY ${runtime_output_directory})
    FILE(COPY_FILE ${CMAKE_CURRENT_LIST_DIR}/coi-serviceworker.js ${runtime_output_directory}/coi-serviceworker.js)

    target_link_options(demo_imgui_bundle PUBLIC -sPTHREAD_POOL_SIZE=2)
endif()
