import streamlit as st
import json

# Function to prettify JSON-LD
def prettify_json_ld(json_ld_str):
    try:
        # Parse JSON-LD string
        parsed_json = json.loads(json_ld_str)
        # Pretty-print JSON-LD
        prettified_json = json.dumps(parsed_json, indent=4)
        return prettified_json
    except json.JSONDecodeError:
        return "Invalid JSON-LD format. Please check your input."

# Streamlit app
st.title("JSON-LD Prettifier")

st.write("Paste your JSON-LD code below and click on 'Prettify' to get the formatted JSON-LD.")

# Text area for user input
json_ld_input = st.text_area("Enter your JSON-LD code here", height=300)

# Button to prettify JSON-LD
if st.button("Prettify"):
    prettified_json_ld = prettify_json_ld(json_ld_input)
    st.code(prettified_json_ld, language="json")

    # Display a copy button if the JSON-LD is valid
    if prettified_json_ld != "Invalid JSON-LD format. Please check your input.":
        st.download_button("Download Prettified JSON-LD", prettified_json_ld, file_name="prettified_json_ld.json", mime="application/json")

st.write("\n\nCreated by: Brandon Lazovic")
