import streamlit as st
from transformers import pipeline, set_seed

# Load GPT-2 generator
generator = pipeline('text-generation', model='gpt2')
set_seed(42)

st.title("Auto Text Prompter with GPT-2")

prompt = st.text_input("Masukkan awal kalimat:", "")

if prompt:
    results = generator(prompt, max_length=50, num_return_sequences=3)
    st.subheader("Hasil Prediksi:")
    for i, res in enumerate(results):
        st.markdown(f"**{i+1}.** {res['generated_text']}")
