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
        self.columnconfigure((0, 1), weight = 1)
        self.rowconfigure(0, weight = 1)
        
        # frame to put entries
        self.main_frame = ctk.CTkFrame(self, width = 400, height = 500)
        self.main_frame.grid(row = 0, column = 0)
        for a in range(5):
            self.main_frame.grid_columnconfigure(a, weight = 1)
        for b in range(6):
            self.main_frame.grid_rowconfigure(b, weight = 1)

        self.enter_frame = ctk.CTkFrame(self, width = 80, height = 520)
        self.enter_frame.grid(row = 0, column = 1)
        for c in range(6):
            self.enter_frame.grid_rowconfigure(c, weight = 1)

        self.entries_list = []
        for i in range(5):
            row_entries = []
            for j in range(6):
                self.entries = ctk.CTkEntry(self.main_frame, width = 60, height = 60, placeholder_text = " ", font = ("Arial", 24), justify = "center")
                self.entries.grid(row = j, column = i, padx = 15, pady = 15)
                row_entries.append(self.entries)
            self.entries_list.append(row_entries)

        for k in range(6):
            self.buttons = ctk.CTkButton(self.enter_frame, text = "+", font = ("Arial", 24), width = 70, height = 70)
            self.buttons.grid(row = k, column = 0, pady = 10)
            


if __name__ == "__main__":
    main = Wordle()
    main.mainloop()