import streamlit as st
import pandas as pd
import plotly.express as px
from transformers import pipeline

# Set page config (must be first)
st.set_page_config(page_title="📊 LLM Data Analyst", page_icon="🧠", layout="wide")

# Load summarizer once
@st.cache_resource
def load_summarizer():
    return pipeline("summarization", model="facebook/bart-large-cnn")

summarizer = load_summarizer()

# Sidebar
with st.sidebar:
    st.title("📁 Upload CSV")
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])
    st.markdown("---")
    st.markdown("💡 Use this tool to chat with your data and generate visual insights using LLM models for free!")

# Main Page
st.title("🧠 LLM-based Automated Data Analyst")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    tab1, tab2, tab3 = st.tabs(["🔍 Preview", "💬 Chat", "📊 Visualize"])

    # --- TAB 1: Preview Data
    with tab1:
        st.subheader("Data Preview")
        st.dataframe(df, use_container_width=True)

        st.subheader("📌 Data Info")
        st.write(f"**Rows:** {df.shape[0]}  |  **Columns:** {df.shape[1]}")
        st.write(f"**Column Names:** `{', '.join(df.columns)}`")

    # --- TAB 2: Chat
    with tab2:
        st.subheader("💬 Ask Questions About the Data")

        if 'messages' not in st.session_state:
            st.session_state.messages = []

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        prompt = st.chat_input("Type your question here...")

        if prompt:
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                with st.spinner("Analyzing with LLM..."):
                    preview_text = df.head(5).to_string(index=False)
                    combined_prompt = f"Dataset Preview:\n{preview_text}\n\nUser Query:\n{prompt}\n\nProvide summarized insight:"
                    combined_prompt = combined_prompt[:1000]  # Limit input
                    summary = summarizer(combined_prompt, max_length=150, min_length=30, do_sample=False)
                    response = summary[0]['summary_text']
                    st.markdown(response)
                    st.session_state.messages.append({"role": "assistant", "content": response})

    # --- TAB 3: Visualize
    with tab3:
        st.subheader("📊 Create a Scatter Plot")
        numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns.tolist()

        if len(numeric_cols) >= 2:
            col1, col2 = st.columns(2)
            with col1:
                x_axis = st.selectbox("Select X-axis", numeric_cols)
            with col2:
                y_axis = st.selectbox("Select Y-axis", numeric_cols, index=1)

            chart = px.scatter(df, x=x_axis, y=y_axis, title=f"{x_axis} vs {y_axis}")
            st.plotly_chart(chart, use_container_width=True)
        else:
            st.warning("Not enough numeric columns to plot a graph.")

else:
    st.info("Upload a CSV file to begin.")
