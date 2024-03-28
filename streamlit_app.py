import streamlit as st

# WARNING: Hardcoded credentials are for demonstration purposes ONLY.
# In a production environment, implement secure authentication using
# password hashing, databases, or external services.

# Session state for authentication
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
    st.session_state["username"] = ""

def login_form():
    username = st.text_input("Username:")
    password = st.text_input("Password:", type="password")

    login_button = st.button("Login")

    if login_button:
        # Simulate authentication (replace with actual authentication logic)
        if username == "testuser" and password == "testuser":  # INSECURE
            st.session_state["authenticated"] = True
            st.session_state["username"] = username
            st.success("Login successful!")
            print("Authenticated:", st.session_state["authenticated"])
        else:
            st.error("Invalid username or password.")

def landing_page():
    st.title(f"Welcome, {st.session_state['username']}!")
    st.write("This is the landing page. Navigate to your desired reports below:")

    # Report selection with navigation (replace with actual report functions)
    report_options = ["Report 1", "Report 2", "Report 3"]
    selected_report = st.selectbox("Select a report:", report_options)

    if selected_report == "Report 1":
        # Call your Report 1 function here (e.g., report_1())
        st.write("This is the content of Report 1.")
    elif selected_report == "Report 2":
        # Call your Report 2 function here (e.g., report_2())
        st.write("This is the content of Report 2.")
    elif selected_report == "Report 3":
        # Call your Report 3 function here (e.g., report_3())
        st.write("This is the content of Report 3.")

if not st.session_state["authenticated"]:
    login_form()
else:
    landing_page()
