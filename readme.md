<h1>RFA</h1>
<br>
<br>
# Copy source code by 1 click!
```
import tkinter as tk
from tkinter import filedialog, Text
import os


root = tk.Tk()
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]
        print(apps)


def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(
        initialdir="/", title="Get acces to files", filetypes=(("all files", "*.*"), ("all files", "*.*")))
    apps.append(filename)
    print(apps)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()


def runApps():
    for app in apps:
        os.startfile(app)


canvas = tk.Canvas(root, height=700, width=700, bg="#3399CC")
canvas.pack()

frame = tk.Frame(root, bg="#996600")
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

openFile = tk.Button(root, text="Open File Browser", padx=25,
                     pady=10, fg='Black', bg="#FF66FF", command=addApp)
openFile.pack()




for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()


root.mainloop()


with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')


```
