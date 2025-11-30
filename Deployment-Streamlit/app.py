import streamlit as st
from agent.coordinator_agent import CoordinatorAgent

st.title("Research Concierge Agent")

session_id = "demo-session"
coordinator = CoordinatorAgent()

uploaded = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded:
    pdf_path = f"uploaded.pdf"
    with open(pdf_path, "wb") as f:
        f.write(uploaded.read())
    
    st.write("Processing PDF...")
    result = coordinator.process_pdf(session_id, pdf_path)

    st.subheader("Extracted Summary")
    st.write(result)
