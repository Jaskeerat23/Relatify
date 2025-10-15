import streamlit as st
from typing import Optional

# Import your organizer functions. Adjust names/paths if your file is named differently.
# Example assumes functions are in Organizer_createFest.py or Organizer.py and available in module Organizer.
# If your file is Organizer_createFest.py, change the import to: from Organizer_createFest import createFest, viewFestDetails, addArtistToEvent, updateFestInfo, festAnalytics
from organizer import createFest, viewFestDetails, addArtistToEvent, updateFestInfo, festAnalytics

st.set_page_config(page_title="Relatify Organizer Dashboard", layout="wide")
st.title("Relatify — Organizer Dashboard")

# Simulated organizer login (for now)
organizer_id = st.number_input("Enter your Organizer ID", min_value=1, step=1)

st.write("---")

if not organizer_id:
    st.warning("Please enter your Organizer ID to proceed.")
    st.stop()

tabs = st.tabs([
    "Create Fest",
    "My Fests",
    "Add Artist to Event",
    "Update Fest",
    "Analytics",
    "About"
])

# -------------------
# TAB: Create Fest
# -------------------
with tabs[0]:
    st.header("Create Fest")
    with st.form("create_fest_form"):
        fest_name = st.text_input("Fest Name", max_chars=100)
        city = st.text_input("City")
        start_date = st.text_input("Start Date (YYYY-MM-DD)")
        description = st.text_area("Description")
        n_events = st.number_input("Number of events to create (n)", min_value=0, step=1, value=0)

        submit = st.form_submit_button("Create Fest")
        if submit:
            if not fest_name:
                st.error("Fest Name is required.")
            else:
                # Use a wrapper that collects event info if n_events > 0
                if n_events > 0:
                    st.info(f"After pressing OK, you will be asked {n_events} times to enter event details in the terminal/console.")
                    # For simplicity, we call createFest which uses input() prompts in console.
                    # If you'd rather have in-UI event creation, we can extend this later.
                result = createFest(int(organizer_id),int(n_events))
                if result.get("status") == "success":
                    st.success(f"Fest created successfully. FestId: {result.get('fest_id')}")
                else:
                    st.error(f"Error creating fest: {result.get('message')}")

    st.markdown("**Note:** Current implementation may prompt in the terminal for event details when `n > 0` because `createFest` uses `input()` for events. If you want the whole flow inside Streamlit UI (event fields in the web page), I can provide that variant.")

# -------------------
# TAB: My Fests
# -------------------
with tabs[1]:
    st.header("Fests Created by You")
    if st.button("Refresh Fests"):
        pass  # refresh controlled below

    res = viewFestDetails(int(organizer_id))
    if isinstance(res, dict) and res.get("status") == "success":
        fests = res.get("fests", [])
    else:
        # If function returns list directly (older variant), handle that
        if isinstance(res, list):
            fests = res
        else:
            st.error(f"Error fetching fests: {res.get('message') if isinstance(res, dict) else res}")
            fests = []

    if not fests:
        st.info("You have not created any fests yet.")
    else:
        for fest in fests:
            # fest may be dict or tuple depending on your cursor type
            if isinstance(fest, dict):
                fid = fest.get("FestId")
                name = fest.get("FestName")
                city = fest.get("City")
                sdate = fest.get("StartDate")
                desc = fest.get("DescriptionFest")
            else:
                # tuple fallback: adapt positions (FestId, FestName, City, StartDate, DescriptionFest)
                fid = fest[0]
                name = fest[1]
                city = fest[2]
                sdate = fest[3]
                desc = fest[4]

            st.subheader(f"{name} (ID: {fid})")
            st.write("City:", city)
            st.write("Start Date:", sdate)
            st.write("Description:", desc)
            st.markdown("---")

# -------------------
# TAB: Add Artist to Event
# -------------------
with tabs[2]:
    st.header("Add Artist to Event")
    with st.form("add_artist_form"):
        event_id = st.number_input("Event ID", min_value=1, step=1)
        artist_id = st.number_input("Artist ID", min_value=1, step=1)
        submit = st.form_submit_button("Add Artist")
        if submit:
            result = addArtistToEvent(int(event_id), int(artist_id))
            if isinstance(result, dict):
                if result.get("status") == "success":
                    st.success(result.get("message"))
                elif result.get("status") == "exists":
                    st.warning(result.get("message"))
                else:
                    st.error(result.get("message"))
            else:
                # if function returns simple strings
                st.write(result)

# -------------------
# TAB: Update Fest
# -------------------
with tabs[3]:
    st.header("Update Fest Info")
    with st.form("update_fest_form"):
        fest_id_upd = st.number_input("Fest ID to update", min_value=1, step=1)
        # fetch current values for display
        if st.form_submit_button("Load Current Values"):
            # call viewFestDetails to get the fest row
            cur_res = viewFestDetails(int(organizer_id))
            target = None
            if isinstance(cur_res, dict) and cur_res.get("status") == "success":
                for f in cur_res.get("fests", []):
                    fid = f.get("FestId") if isinstance(f, dict) else f[0]
                    if fid == int(fest_id_upd):
                        target = f
                        break
            if not target:
                st.error("Fest not found or you are not the owner.")
            else:
                st.write("Current values:")
                if isinstance(target, dict):
                    st.write("FestName:", target.get("FestName"))
                    st.write("City:", target.get("City"))
                    st.write("StartDate:", target.get("StartDate"))
                    st.write("Description:", target.get("DescriptionFest"))
                else:
                    st.write(target)

        st.write("Enter new values (leave blank to keep current):")
        new_name = st.text_input("New Fest Name")
        new_city = st.text_input("New City")
        new_date = st.text_input("New Start Date (YYYY-MM-DD)")
        new_desc = st.text_area("New Description")
        do_update = st.form_submit_button("Update Fest")

        if do_update:
            # If no input provided, use empty dict and the function will keep old values
            new_values = {}
            if new_name:
                new_values["FestName"] = new_name
            if new_city:
                new_values["City"] = new_city
            if new_date:
                new_values["StartDate"] = new_date
            if new_desc:
                new_values["DescriptionFest"] = new_desc

            if not new_values:
                st.info("No changes provided.")
            else:
                # call the non-interactive update function if you have one; otherwise call updateFestInfo which prompts
                try:
                    # if updateFestInfo in your module expects only festId and interactively prompts, call it
                    # if you implemented the dict-based update earlier, prefer calling with new_values
                    # We'll try both: prefer a callable that accepts (festId, newValues)
                    updated = None
                    try:
                        updated = updateFestInfo(fest_id_upd, new_values, orgId=int(organizer_id), confirm=True)
                    except TypeError:
                        # fallback to interactive version (prompting in terminal)
                        updateFestInfo(fest_id_upd)
                        updated = {"status": "success", "message": "Updated via interactive prompt"}
                    if isinstance(updated, dict) and updated.get("status") == "success":
                        st.success("Fest updated successfully.")
                    else:
                        st.write(updated)
                except Exception as e:
                    st.error(f"Error updating fest: {e}")

# -------------------
# TAB: Analytics
# -------------------
with tabs[4]:
    st.header("Organizer Analytics")
    if st.button("Show Analytics"):
        res = festAnalytics(int(organizer_id))
        if isinstance(res, dict) and res.get("status") == "success":
            d = res["data"]
            st.metric("Total Fests", d.get("total_fests", 0))
            st.metric("Total Events", d.get("total_events", 0))
            st.metric("Tickets Sold", d.get("total_tickets_sold", 0))
            st.metric("Total Revenue", f"{d.get('total_revenue', 0):.2f}")
        else:
            st.error(f"Error fetching analytics: {res.get('message') if isinstance(res, dict) else res}")

# -------------------
# TAB: About
# -------------------
with tabs[5]:
    st.header("About Organizer Dashboard")
    st.markdown("""
    Features:
    - Create fests and events (interactive)
    - View fests you created
    - Add artist to an event
    - Update fest details
    - See analytics (total fests, events, tickets, revenue)

    Notes:
    - The `createFest` function currently uses interactive console input for event details if `n > 0`.
      I can change the flow so event details are collected inside the Streamlit form itself (recommended).
    - If your Organizer functions have different function signatures, adjust the import statements accordingly.
    """)

