import streamlit as st
from main import ragassistant


@st.cache_resource
def load_app():
    return ragassistant()


app = load_app()

st.title("RAG Assistant")
st.write("Ask questions about your documents.")

question = st.text_input("Ask a question")

if st.button("Ask"):
    if question.strip():
        with st.spinner("Searching the document and generating answer..."):
            answer = app.ask(question)

        st.subheader("Answer")
        st.write(answer)
    else:
        st.warning("Please enter a question.")