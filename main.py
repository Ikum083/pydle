# Pydle: Python Wordle Clone
# importing modules
import customtkinter as ctk
from random import randint

# window size
window_size = "600x800"

 # list to contain all words to be used
with open("words.txt") as f:
    words = [line.strip() for line in f]

class Wordle(ctk.CTk):
    def __init__(self):
        super().__init__()
        # setting up window
        self.geometry(window_size)
        self.title("Pydle")
        self.resizable(False, False)

if __name__ == "__main__":
    main = Wordle()
    main.mainloop()