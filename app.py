import streamlit as st
from streamlit_ace import st_ace
import subprocess

st.title("Python Code Executor")

# Code editor with syntax highlighting and basic autocompletion
code = st_ace(
    language="python",
    theme="monokai",
    keybinding="vscode",
    font_size=24,
    tab_size=4,
    show_gutter=True,
    wrap=True,
    auto_update=True,
    readonly=False,
)

if st.button("Run"):
    if code:
        # Save the code to a temporary file
        with open("temp_code.py", "w") as f:
            f.write(code)
        
        # Execute the code and capture the output
        result = subprocess.run(["python", "temp_code.py"], capture_output=True, text=True)
        
        # Display the output
        st.subheader("Output:")
        st.text(result.stdout)
        
        # Display errors, if any
        if result.stderr:
            st.subheader("Errors:")
            st.text(result.stderr)
    else:
        st.warning("Please enter some Python code to run.")
