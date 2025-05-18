import streamlit as st
import requests

# Backend endpoint
BACKEND = "http://backend:8000"

st.title("EdTech AI Marketing Agents")
agent = st.selectbox("Run individual agent", [
    "Researcher", "Content Creator","Social Media Manager", "Email Marketer", "Manager"]) # "social"

if st.button("Run Agent"):
    try:
        res = requests.post(f"{BACKEND}/run-agent", json={"agent_name": agent})
        res.raise_for_status()
        result = res.json()["result"]

        # Extract raw text
        raw_text = result.get("raw") or result.get("tasks_output", [{}])[0].get("raw", "")
        formatted_text = raw_text.replace("\\n", "\n")

        # Display result
        st.markdown("### 📊 Agent Output Summary")
        st.markdown(formatted_text)

        # Download result
        st.download_button(
            label="📥 Download Result",
            data=formatted_text,
            file_name=f"{agent}_output.txt",
            mime="text/plain"
        )

    except requests.exceptions.RequestException as e:
        st.error(f"Request failed: {e}")
    except ValueError:
        st.error("Invalid JSON response from backend.")

