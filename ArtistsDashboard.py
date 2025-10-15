import streamlit as st
from Artists import (
    showMyEvents,
    showFavCount,
    updateContractFee,
    showMyInfo
)


st.set_page_config(page_title="Relatify Artist Dashboard", page_icon="🎤", layout="wide")

st.title("🎤 Relatify Artist Dashboard")
st.markdown("Welcome to your personalized artist dashboard!")


artist_id = st.number_input("Enter your Artist ID", min_value=1, step=1)
st.divider()

if artist_id:
    tab1, tab2, tab3, tab4 = st.tabs([
        " Upcoming Events",
        "Favourite Count",
        "Update Contract Fee",
        " Profile Information",
    ])

    
    with tab1:
        st.subheader("Your Upcoming Events")
        events = showMyEvents(artist_id)
        if events:
            for event in events:
                st.write(f"• {event['EventName']} on {event['EventDate']} at {event['EventTime']} — Fest: {event['FestName']} ({event['City']})")
        else:
            st.info("No upcoming events found.")

    
    with tab2:
        st.subheader(" Number of Users Who Marked You as Favourite")
        fav_count = showFavCount(artist_id)
        st.write(f"Total Favourite Count: {fav_count}")

    
    with tab3:
        st.subheader(" Update Your Contract Fee")

        new_fee = st.number_input("Enter New Contract Fee", min_value=0.0, step=100.0, format="%.2f")
        password = st.text_input("Enter Your Password", type="password")

        if st.button("Update Fee"):
            if password:
                result = updateContractFee(artist_id, new_fee, password)
                if "successfully" in result.lower():
                    st.success(result)
                else:
                    st.error(result)
            else:
                st.warning("Please enter your password to update.")


    with tab4:
        st.subheader("Your Profile Information")
        role = st.radio("View As", options=["Admin", "User"], index=1)
        role_param = None if role == "Admin" else "user"

        info = showMyInfo(artist_id, role_param)
        if info:
            st.json(info)
        else:
            st.info("Artist profile not found.")

else:
    st.warning("Please enter a valid Artist ID to access your dashboard.")
