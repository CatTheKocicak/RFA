import os
from tkinter import filedialog

filedialog.askopenfilename(
        initialdir="/", title="Get acces to files", filetypes=(("all files", "*.*"), ("all files", "*.*")))

