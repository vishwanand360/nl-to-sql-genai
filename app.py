import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000/query"

st.set_page_config(page_title="NL to SQL", layout="centered")

st.title("🧠 Natural Language → SQL")
st.write("Ask questions in plain English. Powered by Claude + FastAPI.")

question = st.text_input(
    "Enter your question",
    placeholder="e.g. Show all users"
)

if st.button("Run Query"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Generating SQL and fetching data..."):
            response = requests.post(
                API_URL,
                json={"sql_query": question}
            )

        if response.status_code == 200:
            result = response.json()

            st.subheader("Generated SQL")
            st.code(result["generated_sql"], language="sql")

            st.subheader(f"Results ({result['row_count']} rows)")
            if result["row_count"] > 0:
                df = pd.DataFrame(result["data"])
                st.dataframe(df, use_container_width=True)
            else:
                st.info("No results found.")
        else:
            st.error(response.text)
