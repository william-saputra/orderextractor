import re
import streamlit as st
import pyperclip

# Function to extract product lines and katalog

def extract_product_info(order_text):
    # Use regex to find all product lines (BH)
    product_lines = re.findall(r'(BH\s[^\n]+)', order_text)

    # Use regex to find all KATALOG lines
    katalog_lines = re.findall(r'(KATALOG\s[^\n]+)', order_text)

    # Combine results
    extracted_lines = product_lines + katalog_lines

    # Join all extracted lines into a single string
    return "\n".join(extracted_lines)

# Streamlit app
st.title("Order Information Extractor")

# Input field for the user to paste the order data
order_text = st.text_area("Paste the extracted order text here:")

# Button to trigger extraction
if st.button("Extract"):
    if order_text:
        # Extract product info from the provided text
        result = extract_product_info(order_text)
        st.subheader("Extracted Product and Katalog Information:")
        st.text(result)

        # Add a "Copy to Clipboard" button
        if st.button("Copy to Clipboard"):
            pyperclip.copy(result)  # Copy the extracted text to clipboard
            st.success("Product and Katalog information copied to clipboard!")
    else:
        st.warning("Please enter the order text!")