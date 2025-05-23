import streamlit as st
from database import init_db, add_lead, get_all_leads
from scraper import scrape_cyberbackground  # Your actual scraper function
from datetime import datetime

# Initialize DB once
init_db()

st.title("🏠 Total Leads Finder")

address = st.text_input("Enter fire address (e.g. 123 Main St)")

if st.button("Search Owner Info") and address.strip():
    st.info("Searching... Please wait.")

    # Call your scraper (replace with actual scraper call)
    result = scrape_cyberbackground(address.strip())

    # Example result structure expected from scraper:
    # {
    #   "owner_name": "John Doe",
    #   "phone": "555-1234",
    #   "email": "john@example.com",
    #   "occupancy": "Owner Occupied" or "Renter"
    # }

    if not result:
        st.error("No data found for this address.")
    else:
        occupancy = result.get("occupancy", "").lower()
        if "owner" in occupancy:
            # Save to SQLite only if owner occupied
            add_lead(
                address=address.strip(),
                owner_name=result.get("owner_name", ""),
                phone=result.get("phone", ""),
                email=result.get("email", ""),
                occupancy=result.get("occupancy", "")
            )
            st.success(f"Lead saved for owner-occupied property: {result.get('owner_name')}")
        else:
            st.warning("Property is not owner occupied. Lead not saved.")

st.markdown("---")
st.header("📋 Saved Leads")

leads = get_all_leads()

if not leads:
    st.write("No leads saved yet.")
else:
    for lead in leads:
        _, timestamp, addr, owner, phone, email, occupancy = lead
        st.markdown(f"""
        **Address:** {addr}  
        **Owner:** {owner}  
        **Phone:** {phone}  
        **Email:** {email}  
        **Occupancy:** {occupancy}  
        *Added:* {timestamp}  
        ---
        """)

