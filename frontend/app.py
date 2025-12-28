import streamlit as st
import requests

API_BASE_URL = "http://127.0.0.1:8000"

# -------------------------
# SESSION STATE
# -------------------------
if "token" not in st.session_state:
    st.session_state.token = None

# -------------------------
# SIDEBAR
# -------------------------
st.sidebar.title("🐞 Bug Tracker")

page = st.sidebar.radio(
    "Navigate",
    ["Login", "Create Bug", "View Bugs"]
)

st.sidebar.info("""
👋 Demo Credentials

Admin  
- Username: admin  
- Password: admin123  

Tester  
- Username: tester  
- Password: tester123  

Developer  
- Username: dev  
- Password: dev123  
""")

# -------------------------
# LOGIN PAGE
# -------------------------
if page == "Login":
    st.title("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        response = requests.post(
            f"{API_BASE_URL}/auth/login",
            json={
                "username": username,
                "password": password
            }
        )

        if response.status_code == 200:
            token = response.json()["access_token"]
            st.session_state.token = token
            st.success("Login successful!")
        else:
            st.error("Invalid credentials")

# -------------------------
# CREATE BUG PAGE
# -------------------------
elif page == "Create Bug":
    st.title("🐛 Create Bug")

    if not st.session_state.token:
        st.warning("Please login first")
    else:
        title = st.text_input("Title")
        description = st.text_area("Description")
        priority = st.selectbox("Priority", ["LOW", "MEDIUM", "HIGH"])

        if st.button("Create Bug"):
            response = requests.post(
                f"{API_BASE_URL}/bugs",
                headers={
                    "Authorization": f"Bearer {st.session_state.token}"
                },
                json={
                    "title": title,
                    "description": description,
                    "priority": priority
                }
            )

            if response.status_code == 200:
                st.success("Bug created successfully!")
            else:
                st.error(response.text)

# -------------------------
# VIEW BUGS PAGE
# -------------------------
elif page == "View Bugs":
    st.title("📋 Bug List")

    response = requests.get(f"{API_BASE_URL}/bugs")

    if response.status_code == 200:
        bugs = response.json()

        for bug in bugs:
            st.subheader(f"#{bug['id']} — {bug['title']}")
            st.write(f"Status: {bug['status']}")
            st.write(f"Priority: {bug['priority']}")
            st.write(bug["description"])
            st.divider()
    else:
        st.error("Failed to fetch bugs")
