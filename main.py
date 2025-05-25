import pandas as pd
import tkinter as tk
from tkinter import PhotoImage
import random
import pyttsx3

# Load the dataset
data = pd.read_csv("french_words.csv")
word_list = data.to_dict(orient="records")
to_learn = word_list.copy()
missed_words = []
current_word = {}

# Initialize text-to-speech engine
tts = pyttsx3.init()
tts.setProperty("rate", 140)

# Show next flashcard (English)
def next_card():
    global current_word
    current_word = random.choice(to_learn)
    canvas.itemconfig(card_title, text="English", fill="black")
    canvas.itemconfig(card_word, text=current_word["english"], fill="black")
    window.after(3000, show_translation)

# Flip card to show French translation
def show_translation():
    canvas.itemconfig(card_title, text="French", fill="blue")
    canvas.itemconfig(card_word, text=current_word["french"], fill="blue")
    tts.say(current_word["french"])
    tts.runAndWait()

# User clicked ✔ Correct
def known_word():
    to_learn.remove(current_word)
    next_card()

# User clicked ✘ Wrong
def unknown_word():
    missed_words.append(current_word)
    next_card()

# Save missed words when closing the app
def on_close():
    if missed_words:
        pd.DataFrame(missed_words).to_csv("words_to_learn.csv", index=False)
    window.destroy()

# -------------------- GUI SETUP --------------------
window = tk.Tk()
window.title("Flashcard Translator")
window.config(padx=50, pady=50, bg="#B1DDC6")
window.protocol("WM_DELETE_WINDOW", on_close)

# Load background image
card_bg = PhotoImage(file="card_bg.png")

# Canvas with background
canvas = tk.Canvas(width=800, height=526, bg="#B1DDC6", highlightthickness=0)
canvas.create_image(400, 263, image=card_bg)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"), width=680)
canvas.grid(row=0, column=0, columnspan=3)

# Buttons
wrong_button = tk.Button(text="✘ Wrong", command=unknown_word, width=12)
wrong_button.grid(row=1, column=0, pady=20)

next_button = tk.Button(text="Next", command=next_card, width=12)
next_button.grid(row=1, column=1)

correct_button = tk.Button(text="✔ Correct", command=known_word, width=12)
correct_button.grid(row=1, column=2)

# Start the app
next_card()
window.mainloop()