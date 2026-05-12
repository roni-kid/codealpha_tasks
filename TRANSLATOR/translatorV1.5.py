import customtkinter as ctk
from deep_translator import GoogleTranslator


ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


window = ctk.CTk()
window.title("Language Translator")
window.geometry("500x620")
window.resizable(False, False)
window.configure(fg_color="#f0f4ff")


def safe_translate(text, target):
    try:
        return GoogleTranslator(source='auto', target=target).translate(text)
    except Exception:
        return text

def translate():
    text = input_box.get("1.0", "end").strip()
    source = source_lang.get()
    target = target_lang.get()
    
    if source == "auto detect":
        source = "auto"
    
    result = safe_translate(text, target)
    
    result_box.configure(state="normal")
    result_box.delete("1.0", "end")
    result_box.insert("end", result)
    result_box.configure(state="disabled")

def copy_text():
    window.clipboard_clear()
    window.clipboard_append(result_box.get("1.0", "end").strip())

def clear_all():
    input_box.delete("1.0", "end")
    result_box.configure(state="normal")
    result_box.delete("1.0", "end")
    result_box.configure(state="disabled")
    


title_label = ctk.CTkLabel(
    window,
    text="Language Translator",
    font=("Arial", 22, "bold"),
    text_color="#3d3d8f"
)
title_label.pack(pady=20)


input_frame = ctk.CTkFrame(
    window,
    corner_radius=24,
    fg_color="#ffffff",
    border_width=2,
    border_color="#e8ecff"
)
input_frame.pack(padx=20, pady=8, fill="x")


input_label = ctk.CTkLabel(
    input_frame,
    text="Enter text to translate",
    font=("Arial", 11),
    text_color="#9090bb"
)
input_label.pack(anchor="w", padx=16, pady=(12, 4))

input_box = ctk.CTkTextbox(
    input_frame,
    height=80,
    corner_radius=14,
    fg_color="#f5f7ff",
    border_width=2,
    border_color="#e0e5ff",
    text_color="#3d3d8f",
    font=("Arial", 12)
)
input_box.pack(padx=16, pady=(0, 14), fill="x")


lang_frame = ctk.CTkFrame(
    window,
    corner_radius=24,
    fg_color="#ffffff",
    border_width=2,
    border_color="#e8ecff"
)
lang_frame.pack(padx=20, pady=8, fill="x")

lang_label = ctk.CTkLabel(
    lang_frame,
    text="Languages",
    font=("Arial", 11),
    text_color="#9090bb"
)
lang_label.pack(anchor="w", padx=16, pady=(12, 8))


langs_row = ctk.CTkFrame(lang_frame, fg_color="transparent")
langs_row.pack(padx=16, pady=(0, 14), fill="x")

languages = GoogleTranslator().get_supported_languages()

source_lang = ctk.CTkComboBox(
    langs_row,
    values=["auto detect"] + languages,
    fg_color="#f5f7ff",
    border_color="#e0e5ff",
    button_color="#7c71f0",
    dropdown_fg_color="#ffffff",
    text_color="#3d3d8f",
    width=180
)
source_lang.set("auto detect")
source_lang.pack(side="left")

target_lang = ctk.CTkComboBox(
    langs_row,
    values=languages,
    fg_color="#f5f7ff",
    border_color="#e0e5ff",
    button_color="#7c71f0",
    dropdown_fg_color="#ffffff",
    text_color="#3d3d8f",
    width=180
)
target_lang.set("french")
target_lang.pack(side="right")


translate_btn = ctk.CTkButton(
    window,
    text="Translate",
    font=("Arial", 15, "bold"),
    fg_color="#7c71f0",
    hover_color="#5a4fd4",
    corner_radius=18,
    height=48,
    text_color="#ffffff",
    command=translate
)
translate_btn.pack(padx=20, pady=10, fill="x")


result_frame = ctk.CTkFrame(
    window,
    corner_radius=24,
    fg_color="#ffffff",
    border_width=2,
    border_color="#e8ecff"
)
result_frame.pack(padx=20, pady=8, fill="x")

result_label = ctk.CTkLabel(
    result_frame,
    text="Translation",
    font=("Arial", 11),
    text_color="#9090bb"
)
result_label.pack(anchor="w", padx=16, pady=(12, 4))

result_box = ctk.CTkTextbox(
    result_frame,
    height=80,
    corner_radius=14,
    fg_color="#f5f7ff",
    border_width=2,
    border_color="#e0e5ff",
    text_color="#6060aa",
    font=("Arial", 12),
    state="disabled"
)
result_box.pack(padx=16, pady=(0, 14), fill="x")


bottom_row = ctk.CTkFrame(window, fg_color="transparent")
bottom_row.pack(padx=20, pady=8, fill="x")

copy_btn = ctk.CTkButton(
    bottom_row,
    text="Copy",
    font=("Arial", 13, "bold"),
    fg_color="#ffffff",
    hover_color="#e8ecff",
    corner_radius=16,
    height=40,
    text_color="#7c71f0",
    border_width=2,
    border_color="#e0e5ff",
    command=copy_text
)
copy_btn.pack(side="left", expand=True, fill="x", padx=(0, 6))

clear_btn = ctk.CTkButton(
    bottom_row,
    text="Clear",
    font=("Arial", 13, "bold"),
    fg_color="#ffffff",
    hover_color="#e8ecff",
    corner_radius=16,
    height=40,
    text_color="#7c71f0",
    border_width=2,
    border_color="#e0e5ff",
    command=clear_all
)
clear_btn.pack(side="right", expand=True, fill="x", padx=(6, 0))


window.mainloop()

# aujourd'hui va être un jour heureux