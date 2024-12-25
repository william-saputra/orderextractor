import re
import streamlit as st
import pyperclip

def extract_product_info(order_text):
    # 1) Extract BH lines
    product_lines = re.findall(r'(BH\s[^\n]+)', order_text)

    # 2) Extract lines that contain "katalog" in any case
    #    We use MULTILINE so we can capture lines properly
    raw_katalog_lines = re.findall(r'^.*katalog.*$', order_text, flags=re.IGNORECASE | re.MULTILINE)

    # 3) Clean up each KATALOG line so that it becomes something like "KATALOG 1M"
    katalog_lines = []
    for line in raw_katalog_lines:
        # Look for a quantity pattern, e.g. "1M", "2L", "10P", etc.
        match = re.search(r'(\d+\s*[A-Za-z]+)', line)
        if match:
            # e.g. "1M" or "10pcs"
            quantity = match.group(1).strip()
            katalog_lines.append(f"KATALOG {quantity}")
        else:
            # Fallback if we don't find a quantity
            katalog_lines.append("KATALOG")

    # Combine BH lines + cleaned KATALOG lines
    extracted_lines = product_lines + katalog_lines

    # Return all extracted info in one string
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
            pyperclip.copy(result)
            st.success("Product and Katalog information copied to clipboard!")
    else:
        st.warning("Please enter the order text!")
