import streamlit as st
from streamlit_ace import st_ace
import streamlit_execute as se
import asyncio
import time

st.title("👩‍💻Pythonじっけんしつ 💯")

if "code" not in st.session_state:
    st.session_state["code"] = ""


# Code editor
writing_code = st_ace(
    placeholder="コードを書いてね！",
    value = "print('Hello, World!')",
    language="python",
    theme="monokai",
    keybinding="vscode",
    font_size=20,
    tab_size=4,
    show_gutter=True,
    wrap=True,
    auto_update=True,
    readonly=False,
)

if st.button("じっこう！！ 🚀"):
    st.session_state["code"] = writing_code
#execute code
if st.session_state["code"] == "" or st.session_state["code"] != writing_code:
    st.info("コードを編集中...🖊️")
else:
    response = se.init(writing_code)
    if(response["status"] == "success"):
        if(response["stdout"] == ""):
            st.info("コードにエラーはなかったよ！でも何も表示されないプログラムだね 🤔")
        else:
            st.success("けっか 🎉")
            st.code(response["stdout"], language="python", line_numbers=True)
    elif(response["status"] == "error"):
        st.error("コードにエラーがあったみたい！ 🐛")
    else:
        st.info("じっこうちゅう...🐍")