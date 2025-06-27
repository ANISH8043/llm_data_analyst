# 📊 LLM-based Automated Data Analyst (Chat + Visual Insights)

This is a beginner-friendly, open-source **Streamlit web app** that allows you to upload a CSV file and get:

- 📌 Automatic data summary powered by **Hugging Face LLM** (`facebook/bart-large-cnn`)
- 💬 Chat-based interaction with the dataset (preview-based)
- 📈 Interactive visualizations with **Plotly**
- 🧾 Downloadable analysis summary (optional)
- ☁️ Easy deployment support (Streamlit Cloud, Hugging Face Spaces)

---

## 🔧 Features

| Feature                   | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| 📂 CSV Upload            | Upload your own dataset and preview the data                               |
| 💬 Chat with Data        | Ask questions about the dataset and get insights using an LLM summarizer    |
| 📊 Graph Generation      | Create scatter plots based on selected numeric columns                      |
| 📋 Basic Stats           | Get number of rows, columns, and column names                               |
                                         
---

## 📦 Tech Stack

- **Frontend:** [Streamlit](https://streamlit.io/)
- **NLP:** [Hugging Face Transformers](https://huggingface.co/transformers/) (`facebook/bart-large-cnn`)
- **Visualization:** [Plotly Express](https://plotly.com/python/plotly-express/)
- **PDF Export:** [ReportLab (optional)](https://www.reportlab.com/opensource/)
- **Language:** Python 3.10+

---

## 🚀 Demo (Live App)

> 🧪 Coming soon – deployed on Streamlit Cloud or Hugging Face Spaces

---

## 🛠️ Setup Instructions (Local Development)

### 1. 🔁 Clone the Repository

```bash
git clone https://github.com/ANISH8043/llm_data_analyst.git
cd llm_data_analyst
