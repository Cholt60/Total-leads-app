import streamlit as st
from scraper import scrape_cyberbackground

st.set_page_config(page_title="Total Leads App", layout="centered")
st.title("🏠 Total Leads Finder")

st.markdown("Paste in the **structure fire address** from PulsePoint:")

address = st.text_input("Fire Address")

if st.button("Search Owner Info") and address:
    st.info("Searching CyberBackgroundChecks...")
    result = scrape_cyberbackground(address)

    if "error" in result:
        st.error(result["error"])
    else:
        st.markdown("### 🔍 Results")
        st.markdown(f"**Owner:** {result['owner_name']}")
        st.markdown(f"**Phone:** {result['phone']}")
        st.markdown(f"**Email:** {result['email']}")
        st.markdown(f"**Occupancy Status:** {result['occupancy']}")

        if "Owner" in result['occupancy']:
            st.success("✅ Owner Occupied — Lead saved.")
        else:
            st.warning("⚠️ Renter — Lead skipped.")
