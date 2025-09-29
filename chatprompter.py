import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline, set_seed

# Load GPT2 Indonesia
@st.cache_resource
def load_model():
    model_name = "cahya/gpt2-small-indonesian-522M"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    return pipeline("text-generation", model=model, tokenizer=tokenizer)
#---------

generator = load_model()
set_seed(42)

# UI
st.title("Auto Text Prompter Bahasa Indonesia 🇮🇩")
prompt = st.text_input("Masukkan awal kalimat (misalnya: Saya ingin pergi ke)", "")

if prompt:
    st.subheader("Prediksi Kelanjutan:")
    results = generator(prompt, max_length=50, num_return_sequences=3)
    for i, res in enumerate(results):
        st.markdown(f"**{i+1}.** {res['generated_text']}")
