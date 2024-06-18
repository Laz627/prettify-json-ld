import streamlit as st
import json
import re

# Function to extract JSON-LD from script tag
def extract_json_ld(script_str):
    try:
        # Use regex to find all JSON objects within the script tag
        json_objects = re.findall(r'\{.*?\}', script_str, re.DOTALL)
        if json_objects:
            return json_objects
        else:
            return None
    except ValueError:
        return None

# Function to prettify JSON-LD
def prettify_json_ld(json_ld_str):
    try:
        # Parse JSON-LD string
        parsed_json = json.loads(json_ld_str)
        # Pretty-print JSON-LD
        prettified_json = json.dumps(parsed_json, indent=4, ensure_ascii=False)
        return prettified_json
    except json.JSONDecodeError as e:
        return f"Invalid JSON-LD format. Error: {e}"

# Streamlit app
st.title("JSON-LD Prettifier")

st.write("Paste your JSON-LD code below and click on 'Prettify' to get the formatted JSON-LD.")

# Text area for user input
json_ld_input = st.text_area("Enter your JSON-LD code here", height=300)

# Button to prettify JSON-LD
if st.button("Prettify"):
    # Extract JSON-LD from script tag
    json_ld_objects = extract_json_ld(json_ld_input.strip())
    if json_ld_objects:
        prettified_jsons = [prettify_json_ld(obj) for obj in json_ld_objects]
        prettified_json_ld = '\n\n'.join(prettified_jsons)
    else:
        prettified_json_ld = "Invalid JSON-LD format. Please ensure you have pasted the correct code."

    st.code(prettified_json_ld, language="json")

    # Display a copy button if the JSON-LD is valid
    if not prettified_json_ld.startswith("Invalid JSON-LD format."):
        st.download_button("Download Prettified JSON-LD", prettified_json_ld, file_name="prettified_json_ld.json", mime="application/json")

st.write("\n\nCreated by: Brandon Lazovic")
