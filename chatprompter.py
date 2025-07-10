import tkinter as tk
from transformers import pipeline, set_seed

# Load GPT-2 pipeline
generator = pipeline('text-generation', model='gpt2')
set_seed(42)  # Untuk hasil konsisten

def generate_text():
    prompt = entry.get()
    result = generator(prompt, max_length=50, num_return_sequences=3)
    
    listbox.delete(0, tk.END)
    for i, output in enumerate(result):
        listbox.insert(tk.END, f"{i+1}. {output['generated_text']}")

# GUI setup
root = tk.Tk()
root.title("Generative Auto Text Prompter (GPT-2)")

tk.Label(root, text="Ketik awal kalimat:").pack(pady=5)

entry = tk.Entry(root, width=60)
entry.pack(padx=10, pady=5)

tk.Button(root, text="Lanjutkan dengan GPT-2", command=generate_text).pack(pady=5)

listbox = tk.Listbox(root, width=80)
listbox.pack(padx=10, pady=5)

root.mainloop()
