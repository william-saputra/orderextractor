import re
import streamlit as st
import pyperclip

# Function to extract product lines
def extract_product_info(order_text):
    # Use regex to find all product lines
    product_lines = re.findall(r'(BH\s[^\n]+)', order_text)
    # Join all extracted lines into a single string
    return "\n".join(product_lines)

# Streamlit app
st.title("Order Information Extractor")

# Input field for the user to paste the order data
order_text = st.text_area("Paste the extracted order text here:")

# Button to trigger extraction
if st.button("Extract"):
    if order_text:
        # Extract product info from the provided text
        result = extract_product_info(order_text)
        st.subheader("Extracted Product Information:")
        st.text(result)

        # Add a "Copy to Clipboard" button
        if st.button("Copy to Clipboard"):
            pyperclip.copy(result)  # Copy the extracted text to clipboard
            st.success("Product information copied to clipboard!")
    else:
        st.warning("Please enter the order text!")
