import streamlit as st
from crew import crew







# Streamlit App
st.title("Customer Support Automation")

# Input Fields
customer_name = st.text_input("Customer Name:")
customer_company = st.text_input("company:")
inquiry = st.text_area("Customer Inquiry:")

# Submit Button
if st.button("Submit Inquiry"):
    inputs = {
        "customer": customer_name,
        "company": customer_company,
        "inquiry": inquiry,
    }

    # Run Crew with Inputs
    result = crew.kickoff(inputs=inputs)

    # Display Response
    st.success("**Response:**")
    st.markdown(result)
   
