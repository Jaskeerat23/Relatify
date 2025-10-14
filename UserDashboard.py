import streamlit as st
from Users import (
    UserFavArtistsFests,
    UserCityFests,
    listFests,
    ticketsPurchased,
    festUserAttended,
    addArtistFav,
    removeFromFav,
    changeUserName
)

# --- Streamlit Page Config ---
st.set_page_config(page_title="Relatify Dashboard", page_icon="🎵", layout="wide")

st.title("🎵 Relatify User Dashboard")
st.markdown("Welcome to your personalized fest dashboard!")

# --- Simulated Login (for now) ---
user_id = st.number_input("Enter your User ID", min_value=1, step=1)
st.divider()

if user_id:
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "🏕️ Fests (Based on Favourites & City)",
        "🎟️ Tickets Purchased",
        "✅ Fests Attended",
        "⭐ Manage Favourites",
        "🧑‍💻 Change Username",
        "ℹ️ About"
    ])

    # --- TAB 1: Fests ---
    with tab1:
        st.subheader("🎤 Fests where your favourite artists are performing")
        favFests, cityFests, otherFests = listFests(user_id)

        if favFests:
            for fest in favFests:
                st.write("•", fest)
        else:
            st.info("No fests found for your favourite artists.")

        st.divider()
        st.subheader("🏙️ Fests happening in your city")
        if cityFests:
            for fest in cityFests:
                st.write("•", fest)
        else:
            st.info("No city fests available currently.")

        st.divider()
        st.subheader("🎡 Other Available Fests")
        if otherFests:
            for fest in otherFests:
                st.write("•", fest)
        else:
            st.info("No other fests at the moment.")

    # --- TAB 2: Tickets Purchased ---
    with tab2:
        st.subheader("🎟️ Your Purchased Tickets")
        tickets, count = ticketsPurchased(user_id)
        st.write(f"Total Tickets Purchased: {count}")
        if tickets:
            st.table(list(tickets))
        else:
            st.info("No tickets purchased yet.")

    # --- TAB 3: Fests Attended ---
    with tab3:
        st.subheader("✅ Fests You Have Attended")
        fests, count = festUserAttended(user_id)
        st.write(f"Total Fests Attended: {count}")
        if fests:
            st.table(list(fests))
        else:
            st.info("You haven’t attended any fests yet.")

    # --- TAB 4: Manage Favourite Artists ---
    with tab4:
        st.subheader("⭐ Manage Favourite Artists")

        artist_id = st.number_input("Enter Artist ID", min_value=1, step=1)
        col1, col2 = st.columns(2)

        with col1:
            if st.button("Add to Favourites"):
                with st.expander("Confirm Action"):
                    if st.button("✅ Confirm Add"):
                        result = addArtistFav(user_id, artist_id, True)
                        st.success(result)
                    elif st.button("❌ Cancel Add"):
                        result = addArtistFav(user_id, artist_id, False)
                        st.warning(result)

        with col2:
            if st.button("Remove from Favourites"):
                with st.expander("Confirm Action"):
                    if st.button("✅ Confirm Remove"):
                        result = removeFromFav(user_id, artist_id, True)
                        st.success(result)
                    elif st.button("❌ Cancel Remove"):
                        result = removeFromFav(user_id, artist_id, False)
                        st.warning(result)

    # --- TAB 5: Change Username ---
    with tab5:
        st.subheader("🧑‍💻 Change Your Username")

        current_name = st.text_input("Current Username")
        new_name = st.text_input("New Username")
        password = st.text_input("Password", type="password")

        if st.button("Change Username"):
            with st.expander("Confirm Username Change"):
                if st.button("✅ Confirm"):
                    result = changeUserName(user_id, current_name, new_name, password, True)
                    st.success(result)
                elif st.button("❌ Cancel"):
                    result = changeUserName(user_id, current_name, new_name, password, False)
                    st.warning(result)

    # --- TAB 6: About Section ---
    with tab6:
        st.markdown("""
        ### About Relatify Dashboard
        This is your all-in-one user dashboard for:
        - Viewing favourite artist fests 🎤  
        - Tracking your city fests 🏙️  
        - Managing tickets 🎟️  
        - Changing username 🧑‍💻  
        - Managing favourite artists ⭐  

        Built with ❤️ using **Streamlit** and **MySQL**.
        """)

else:
    st.warning("Please enter a valid User ID to access your dashboard.")
