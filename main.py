import tkinter as tk
import time

def update_time():
    current_time = time.strftime('%H:%M:%S')
    time_label.config(text=current_time)
    root.after(1000, update_time)

root = tk.Tk()
root.title("Текущее время")
root.geometry("320x140")
root.resizable(False, False)
root.configure(bg="#1e1e1e")

time_label = tk.Label(
    root,
    font=("Helvetica", 46, "bold"),
    bg="#1e1e1e",
    fg="#00ffcc"
)
time_label.pack(expand=True)

update_time()
root.mainloop()
