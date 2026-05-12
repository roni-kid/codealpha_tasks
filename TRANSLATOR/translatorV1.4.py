import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator


def safe_translate(text, target):
    try:
        return GoogleTranslator(source='auto', target=target).translate(text)
    except Exception:
        return text
    
    
def translate():
    text = input_box.get("1.0", tk.END).strip()
    source = source_lang.get()
    target = target_lang.get()
    if source == "auto detect":
        source = "auto"
    result = safe_translate(text, target)
    result_box.config(state="normal")
    result_box.delete("1.0", tk.END)
    result_box.insert(tk.END, result)
    result_box.config(state="disabled")




window = tk.Tk()
window.title("Language Translator")
window.geometry("500x450")
window.resizable(False, False)

title_label = tk.Label(window, text="Language Translator", font=("Arial", 18, "bold"))
title_label.pack(pady=20)

input_label = tk.Label(window, text="Enter text to translate:", font=("Arial", 11))
input_label.pack(anchor="w", padx=20)

input_box = tk.Text(window, height=4, width=55, font=("Arial", 11))
input_box.pack(padx=20, pady=5)

languages = GoogleTranslator().get_supported_languages()

lang_frame = tk.Frame(window)
lang_frame.pack(padx=20, pady=10, fill="x")

source_label = tk.Label(lang_frame, text="From:", font=("Arial", 11))
source_label.grid(row=0, column=0, padx=5)

source_lang = ttk.Combobox(lang_frame, values=["auto detect"] + languages, width=18)
source_lang.set("auto detect")
source_lang.grid(row=0, column=1, padx=5)

target_label = tk.Label(lang_frame, text="To:", font=("Arial", 11))
target_label.grid(row=0, column=2, padx=5)

target_lang = ttk.Combobox(lang_frame, values=languages, width=18)
target_lang.set("french")
target_lang.grid(row=0, column=3, padx=5)

translate_btn = tk.Button(window, text="Translate", font=("Arial", 12, "bold"), width=20, command=translate)
translate_btn.pack(pady=10)

result_label = tk.Label(window, text="Translation:", font=("Arial", 11))
result_label.pack(anchor="w", padx=20)

result_box = tk.Text(window, height=4, width=55, font=("Arial", 11), state="disabled")
result_box.pack(padx=20, pady=5)



window.mainloop()