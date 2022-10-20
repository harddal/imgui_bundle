from imgui_bundle import imgui, imgui_md, static, ImVec2
import code_str_utils
import inspect


def unindent(s: str):
    r = code_str_utils.unindent_code(s, flag_strip_empty_lines=True)
    return r


def md_render_unindent(md: str):
    u = code_str_utils.unindent_code(md, flag_strip_empty_lines=True, is_markdown=True)
    imgui_md.render(u)


class AppState:
    counter = 0
    name = ""


def show_code_advice(python_gui_function, cpp_code):
    import inspect
    python_code = inspect.getsource(python_gui_function)

    code_size = ImVec2(500, 150)

    imgui.begin_group()
    imgui.text("C++ code")
    imgui.input_text_multiline("##C++", unindent(cpp_code), code_size)
    imgui.end_group()
    imgui.same_line()
    imgui.begin_group()
    imgui.text("Python code")
    imgui.input_text_multiline("##Python", unindent(python_code), code_size)
    imgui.end_group()
    python_gui_function()


@static(value=0)
def demo_radio_button():
    static = demo_radio_button
    clicked, static.value = imgui.radio_button("radio a", static.value, 0); imgui.same_line()
    clicked, static.value = imgui.radio_button("radio b", static.value, 1); imgui.same_line()
    clicked, static.value = imgui.radio_button("radio c", static.value, 2);


def show_basic_code_advices():
    cpp_code = """
        void DemoRadioButton()
        {
            static int value = 0;
            ImGui::RadioButton("radio a", &value, 0); ImGui::SameLine();
            ImGui::RadioButton("radio b", &value, 1); ImGui::SameLine();
            ImGui::RadioButton("radio c", &value, 2);
        }
    """

    imgui_md.render("""
    In order to translate from C++ to Python:
     1. change the function names and parameters' names from `CamelCase` to `snake_case`
     2. change the way the output are handled
        a. in C++ `ImGui::RadioButton` modifies its second parameter (which is passed by address) and returns true if the user clicked the radio button
        b. In python, the (possibly modified) value is transmitted via the return: ìmgui.radio_button` returns a `Tuple[bool, str]` which contains (user_clicked, new_value)
    3. if porting some code that uses static variables, use the @static decorator
       In this case, this decorator simply adds a variable "value" at the function scope. It is is preserved between calls.
       Normally, this variable should be accessed via "demo_radio_button.value", however the first line of the function
       adds a synonym named static for more clarity.
       Do not overuse them! Static variable suffer from almost the same shortcomings as global variables, so you should prefer to modify an application state.
    """)
    show_code_advice(demo_radio_button, cpp_code)


@static(is_initialized=False)
def demo_imgui():
    static = demo_imgui

    if not static.is_initialized:
        static.app_state = AppState()
        static.is_initialized = True

    app_state: AppState = static.app_state

    md_render_unindent(
        """
        # imgui-bundle
        [imgui-bundle](https://github.com/pthom/imgui_bundle) is a collection of python bindings for [Dear ImGui](https://github.com/ocornut/imgui.git), and various libraries from its ecosystem.
        The bindings were autogenerated from the original C++ code, so that they are easier to keep up to date, and the python API closely matches the C++ api.
        
        ## Dear ImGui
        [Dear ImGui](https://github.com/ocornut/imgui.git) is one possible implementation of an idea generally described 
        as the IMGUI (Immediate Mode GUI) paradigm.
    """)

    if imgui.collapsing_header("Advices", imgui.ImGuiTreeNodeFlags_.default_open):
        if imgui.tree_node("Immediate mode gui"):
            md_render_unindent("""An example is often worth a thousand words. The following code:""")

            def immediate_gui_example():
                # Display a text
                imgui.text(f"Counter = {app_state.counter}")
                imgui.same_line()  # by default ImGui starts a new line at each widget

                # The following line displays a button
                if imgui.button("increment counter"):
                    # And returns true if it was clicked: you can *immediately* handle the click
                    app_state.counter += 1

            imgui.input_text_multiline("##immediate_gui_example", unindent(inspect.getsource(immediate_gui_example)),
                                       ImVec2(500, 150))
            imgui.text("Displays this:")
            immediate_gui_example()
            imgui.separator()
            imgui.tree_pop()

        if imgui.tree_node("Consult the interactive manual!"):
            md_render_unindent("""
            Dear ImGui comes with a complete demo. It demonstrates all of the widgets, together with an example code on how to use them.

            [ImGui Manual](https://pthom.github.io/imgui_manual_online/manual/imgui_manual.html) is an easy way to consult this demo, and to see the corresponding code. The demo code is in C++, but read-on for advices on how to translate from C++ to python.
            """)
            if imgui.button("Open imgui manual"):
                import webbrowser
                webbrowser.open("https://pthom.github.io/imgui_manual_online/manual/imgui_manual.html")
            imgui.tree_pop()

        if imgui.tree_node("Basic code advices"):
            show_basic_code_advices()
            imgui.tree_pop()

        if imgui.tree_node("TextInput and enums"):
            cpp_code = """
            static char text[64] = ""; 
            ImGui::InputText("decimal", text, 64, ImGuiInputTextFlags_CharsDecimal);
            """

            imgui.text("Bla")
            imgui.tree_pop()

    imgui.separator()
    imgui_md.render("""
## Dear ImGui demo window
The following is the output of imgui.show_demo_window()
(which is also show inside [ImGui Manual](https://pthom.github.io/imgui_manual_online/manual/imgui_manual.html)) 
    """)
    imgui.show_demo_window()
