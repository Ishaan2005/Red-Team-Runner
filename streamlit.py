import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"
   # docker-compose service name

st.title("Red Team Runner Dashboard")

st.write("This dashboard runs a red-team test suite and shows results.")

# --- RUN BUTTON ---
if st.button("Run Test Suite"):
    response = requests.post(
        f"{API_URL}/run",
        json={"suite": "default"}
    )

    if response.status_code == 200:
        run_id = response.json()["run_id"]
        st.success(f"Run started successfully!")
        st.session_state["run_id"] = run_id
    else:
        st.error("Failed to start run")

# --- SHOW REPORT ---
if "run_id" in st.session_state:
    st.write(f"Run ID: {st.session_state['run_id']}")

    if st.button("Get Report"):
        report = requests.get(
            f"{API_URL}/report/{st.session_state['run_id']}"
        )

        if report.status_code == 200:
            data = report.json()

            st.subheader("Summary")
            st.json(data["summary"])

            st.subheader("Results")
            for result in data["results"]:
                st.write(f"Scenario ID: {result['scenario_id']}")
                st.write(f"Status: {result['status']}")

                if result["status"] == "failed":
                    st.write(f"Evidence: {result['evidence']}")

                st.markdown("---")
        else:
            st.error("Could not fetch report")
