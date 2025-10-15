import streamlit as st
from crewmember import showMyEvents, showUpcomingTasks, updateProfile, changePassword, taskStats

st.set_page_config(page_title="Crew Dashboard", page_icon="🧑‍💼", layout="wide")


#  Header

st.title("🧑‍💼 Crew Member Dashboard")
st.write("Manage your profile, view tasks, and check your stats.")

# Sidebar: Member ID Input

st.sidebar.header("🔑 Member Login")
member_id = st.sidebar.number_input("Enter your Member ID", min_value=1, step=1)

if member_id:
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "👤 My Profile", "🗓 Upcoming Tasks", "✏ Update Profile",
        "🔒 Change Password", "📊 Task Stats"
    ])

  
    #  Tab 1: My Profile
  
    with tab1:
        st.subheader("My Profile")
        data = showMyEvents(member_id)
        if isinstance(data, dict):
            st.success("Profile Found ✅")
            st.write(f"*Full Name:* {data['FullName']}")
            st.write(f"*City:* {data['City']}")
            st.write(f"*Role:* {data['Role']}")
            st.write(f"*Date of Joining:* {data['DOJ']}")
        else:
            st.error(data)

    
    #  Tab 2: Upcoming Tasks
    
    with tab2:
        st.subheader("Upcoming Tasks")
        st.info(showUpcomingTasks(member_id))

    
    # Tab 3: Update Profile
   
    with tab3:
        st.subheader("Update Profile Details")

        col1, col2, col3 = st.columns(3)
        with col1:
            new_fname = st.text_input("First Name")
        with col2:
            new_mname = st.text_input("Middle Name (optional)")
        with col3:
            new_lname = st.text_input("Last Name")

        new_email = st.text_input("Email")
        new_phone = st.text_input("Phone Number")
        new_city = st.text_input("City")

        if st.button("💾 Update Profile"):
            if new_fname and new_email and new_phone and new_city:
                msg = updateProfile(member_id, new_fname, new_mname, new_lname, new_email, new_phone, new_city)
                if "successfully" in msg:
                    st.success(msg)
                else:
                    st.error(msg)
            else:
                st.warning("Please fill all required fields.")

    
    # Tab 4: Change Password
 
    with tab4:
        st.subheader("Change Password")

        old_pass = st.text_input("Old Password", type="password")
        new_pass = st.text_input("New Password", type="password")
        confirm_pass = st.text_input("Confirm New Password", type="password")

        if st.button("🔄 Update Password"):
            if new_pass == confirm_pass and new_pass:
                msg = changePassword(member_id, old_pass, new_pass)
                if "successfully" in msg:
                    st.success(msg)
                else:
                    st.error(msg)
            else:
                st.warning("Passwords do not match or are empty.")

    
    # Tab 5: Task Stats
  
    with tab5:
        st.subheader("Task Statistics")
        stats = taskStats(member_id)
        if isinstance(stats, dict):
            st.metric("👤 Name", stats["Name"])
            st.metric("🎭 Role", stats["Role"])
            st.metric("📅 Date of Joining", stats["DOJ"])
            st.metric("✅ Tasks Completed", stats["TasksCompleted"])
            st.metric("🕒 Tasks Pending", stats["TasksPending"])
        else:
            st.error(stats)
else:
    st.info("Please enter your Member ID from the sidebar to begin.")