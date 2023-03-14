import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    words = word_entry.get().split()
    if len(words) < 5:
        messagebox.showerror("Error", "Please enter at least 5 words.")
        return

    selected_words = []
    while len(selected_words) < 3:
        random_word = random.choice(words)
        if random_word not in selected_words:
            selected_words.append(random_word)

    num_pair = [random.randint(0, 9), random.randint(0, 9)]

    special_char = random.choice(string.punctuation)

    combined = selected_words + [f"{num_pair[0]}{special_char}{num_pair[1]}"]
    result_string = ""
    while combined:
        random_index = random.randint(0, len(combined)-1)
        result_string += combined[random_index]
        combined.pop(random_index) 

    vowels = "aeiou"
    result_string = "".join(c.upper() if c.lower() in vowels else c for c in result_string)
    result_label.config(text=result_string)
root = tk.Tk()
root.title("Random Password Generator")
word_label = tk.Label(root, text="Enter 5 random words separated by spaces:")
word_entry = tk.Entry(root)
regen_button = tk.Button(root, text="Regenerate", command=generate_password)
result_label = tk.Label(root, text="", font=("Courier", 16))
word_label.pack()
word_entry.pack()
regen_button.pack()
result_label.pack()

root.mainloop()
