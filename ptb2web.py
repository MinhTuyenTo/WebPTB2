import streamlit as st
import math

st.set_page_config(page_title="Giải phương trình bậc 2", page_icon="🧮", layout="centered")
st.title("Máy giải phương trình bậc 2")

# ----- Khởi tạo session state -----
if "step" not in st.session_state:
    st.session_state.step = "input"  # input -> show_equation -> solved
if "a" not in st.session_state:
    st.session_state.a = 0.0
    st.session_state.b = 0.0
    st.session_state.c = 0.0
if "result" not in st.session_state:
    st.session_state.result = []

# ----- Input inline [ô]x² + [ô]x + [ô] = 0 -----
if st.session_state.step == "input":
    cols = st.columns([1,0.2,1,0.2,1,0.5])
    with cols[0]:
        a = st.number_input("", value=0.0, format="%.2f", key="input_a")
    cols[1].markdown("x² +")
    with cols[2]:
        b = st.number_input("", value=0.0, format="%.2f", key="input_b")
    cols[3].markdown("x +")
    with cols[4]:
        c = st.number_input("", value=0.0, format="%.2f", key="input_c")
    cols[5].markdown("= 0")

    ok_col, reset_col = st.columns(2)
    with ok_col:
        if st.button("OK"):
            st.session_state.a = a
            st.session_state.b = b
            st.session_state.c = c
            st.session_state.step = "show_equation"
    with reset_col:
        if st.button("Nhập lại"):
            st.session_state.input_a = 0.0
            st.session_state.input_b = 0.0
            st.session_state.input_c = 0.0

# ----- Hiển thị phương trình + nút Giải -----
elif st.session_state.step == "show_equation":
    a = st.session_state.a
    b = st.session_state.b
    c = st.session_state.c
    st.markdown(f"**Phương trình:** {a}x² + {b}x + {c} = 0")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Giải"):
            result = []
            if a == 0:
                if b == 0:
                    if c == 0:
                        result.append("Phương trình vô số nghiệm")
                    else:
                        result.append("Phương trình vô nghiệm")
                else:
                    x = -c / b
                    result.append(f"x = {x:.2f}")
            else:
                delta = b**2 - 4*a*c
                if delta < 0:
                    result.append("Phương trình vô nghiệm")
                elif delta == 0:
                    x = -b / (2*a)
                    result.append(f"x = {x:.2f}")
                else:
                    x1 = (-b + math.sqrt(delta)) / (2*a)
                    x2 = (-b - math.sqrt(delta)) / (2*a)
                    result.append(f"x₁ = {x1:.2f}")
                    result.append(f"x₂ = {x2:.2f}")
            st.session_state.result = result
            st.session_state.step = "solved"
    with col2:
        if st.button("Nhập lại"):
            st.session_state.step = "input"
            st.session_state.input_a = 0.0
            st.session_state.input_b = 0.0
            st.session_state.input_c = 0.0

# ----- Hiển thị kết quả + nút Tiếp theo -----
elif st.session_state.step == "solved":
    for r in st.session_state.result:
        st.success(r)

    if st.button("Tiếp theo"):
        st.session_state.step = "input"
        st.session_state.result = []
        st.session_state.input_a = 0.0
        st.session_state.input_b = 0.0
        st.session_state.input_c = 0.0

st.markdown("---")
st.markdown("© Made By MinhTuyen")
