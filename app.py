import streamlit as st

# Simulated scrape function (replace with real scraping logic)
def scrape_cyberbackground(address):
    if "Las Vegas" in address or "Henderson" in address or "North Las Vegas" in address:
        return {
            "owner_name": "Jane Smith",
            "phone": "702-555-9876",
            "email": "jane@example.com",
            "occupancy": "Owner Occupied",
            "notes": "Ready for outreach"
        }
    else:
        return {
            "owner_name": "",
            "phone": "",
            "email": "",
            "occupancy": "Renter Occupied",
            "notes": "Skip for outreach"
        }

st.title("Fire Lead Lookup")

address = st.text_input("Enter Fire Address")

if st.button("Check Occupancy & Owner Info"):
    if not address:
        st.error("Please enter an address")
    else:
        result = scrape_cyberbackground(address)
        st.markdown(f"**Occupancy Type:** {result['occupancy']}")
        st.markdown(f"**Owner Name:** {result['owner_name']}")
        st.markdown(f"**Phone:** {result['phone']}")
        st.markdown(f"**Email:** {result['email']}")
        st.markdown(f"**Notes:** {result['notes']}")
