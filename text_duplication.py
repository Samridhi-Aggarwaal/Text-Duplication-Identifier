# text duplication calcutor with GUI

import tkinter as tk
from tkinter import filedialog
import difflib

def calculate_text_duplication_percentage(file1_path, file2_path):
    with open(file1_path, 'r') as file1:
        text1 = file1.read()
    with open(file2_path, 'r') as file2:
        text2 = file2.read()
    similarity = difflib.SequenceMatcher(None, text1, text2).ratio()
    return similarity * 100
def browse_file1():
    file1_path = filedialog.askopenfilename()
    entry_file1.delete(0, tk.END)
    entry_file1.insert(0, file1_path)

def browse_file2():
    file2_path = filedialog.askopenfilename()
    entry_file2.delete(0, tk.END)
    entry_file2.insert(0, file2_path)
def calculate_and_display_percentage():
    file1_path = entry_file1.get()
    file2_path = entry_file2.get()
    if file1_path and file2_path:
        duplication_percentage = calculate_text_duplication_percentage(file1_path, file2_path)
        result_label.config(text=f"Percentage of text duplication: {duplication_percentage:.2f}%")

window = tk.Tk()
window.title("Text Duplication Calculator")
label_file1 = tk.Label(window, text="Select File 1:")
entry_file1 = tk.Entry(window, width=50)
button_browse_file1 = tk.Button(window, text="Browse", command=browse_file1)
label_file2 = tk.Label(window, text="Select File 2:")
entry_file2 = tk.Entry(window, width=50)
button_browse_file2 = tk.Button(window, text="Browse", command=browse_file2)
result_label = tk.Label(window, text="")
calculate_button = tk.Button(window, text="Calculate Percentage", command=calculate_and_display_percentage)

# Place widgets on the window
label_file1.grid(row=0, column=0)
entry_file1.grid(row=0, column=1)
button_browse_file1.grid(row=0, column=2)
label_file2.grid(row=1, column=0)
entry_file2.grid(row=1, column=1)
button_browse_file2.grid(row=1, column=2)
calculate_button.grid(row=2, column=1)
result_label.grid(row=3, column=0, columnspan=3)
window.mainloop()