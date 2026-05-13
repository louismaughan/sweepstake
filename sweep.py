import streamlit as st
import random
import pandas as pd

st.set_page_config(page_title="World Cup sweepstake", page_icon="🎲")

st.title("🎲 Methods Digital World Cup 2026 sweepstake")
st.write("Enter your players and teams to assign them randomly.")

# Layout: Two columns for data entry
col1, col2 = st.columns(2)

with col1:
    participants_input = st.text_area(
        "Players (one per line)", 
        placeholder="Alex\nLouis\nCharles"
    )

with col2:
    items_input = st.text_area(
        "Teams (one per line)", 
        placeholder="Brazil\nFrance\nEngland"
    )

if st.button("Run sweepstake"):
    # Clean the inputs
    participants = [p.strip() for p in participants_input.split('\n') if p.strip()]
    items = [i.strip() for i in items_input.split('\n') if i.strip()]

    if not participants or not items:
        st.error("Please provide both participants and items!")
    else:
        # Shuffle the items
        random.shuffle(items)
        
        # Logic: Distribute items as evenly as possible
        results = []
        for i, item in enumerate(items):
            # Use modulo to cycle through participants if there are more items than people
            assignee = participants[i % len(participants)]
            results.append({"Player": assignee, "Team": item})
        
        # Display Results
        df = pd.DataFrame(results)
        st.success("Drawing Complete!")
        st.table(df)
        
        # Option to download
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            "Download Results as CSV",
            csv,
            "sweepstake_results.csv",
            "text/csv"
        ) 






