import streamlit as st
from main import ragassistant
from pathlib import Path


@st.cache_resource
def load_app():
    return ragassistant()


app = load_app()

st.title("RAG Assistant")
st.write("Upload a PDF and ask questions about it.")

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    data_folder = Path("data")
    data_folder.mkdir(exist_ok=True)

    file_path = data_folder / uploaded_file.name

    with open(file_path, "wb") as file:
        file.write(uploaded_file.getbuffer())

    app.ingest_document(str(file_path))

    st.success(f"{uploaded_file.name} uploaded and processed successfully.")

question = st.text_input("Ask a question")

if st.button("Ask"):

    if question.strip():

        with st.spinner("Searching the document and generating answer..."):
            answer = app.ask(question)

        st.subheader("Answer")
        st.write(answer)

    else:
        st.warning("Please enter a question.")