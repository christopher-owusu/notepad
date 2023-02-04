import tkinter as tk

def save_file():
    with open("notepad.txt", "w") as file:
        file.write(text.get("1.0", "end"))

root = tk.Tk()
root.title("Notepad")

text = tk.Text(root, wrap="word")
text.pack(fill="both", expand=True)

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Exit", command=root.quit)

root.mainloop()