import streamlit as st
from src.ui.user_data_storage import write_credentials, storage_file, Credentials


def login_page(credentials):
    with st.form("login_form"):
        st.title("登录")
        username = st.text_input("用户名", value="")
        password = st.text_input("密码", value="", type="password")
        submit = st.form_submit_button("登录")
        
        if submit:
            user_cred = credentials.get(username)
            if user_cred and user_cred.password == password:
                st.success("登录成功！")
                st.session_state.logged_in = True
                st.session_state.admin = user_cred.is_admin
                st.session_state.usname = username
                st.rerun()
            else:
                st.error("用户名或密码错误，请重新输入。")


def register_page(credentials):
    with st.form("register_form"):
        st.title("注册")
        new_username = st.text_input("设置用户名", value="")
        new_password = st.text_input("设置密码", value="", type="password")
        is_admin = False
        register_submit = st.form_submit_button("注册")
        
        if register_submit:
            if new_username in credentials:
                st.error("用户名已存在，请使用其他用户名。")
            else:
                new_user = Credentials(new_username, new_password, is_admin)
                credentials[new_username] = new_user
                write_credentials(storage_file, credentials)
                st.success(f"用户 {new_username} 注册成功！请登录。")
                st.rerun()