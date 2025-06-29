#SIMPLE CALCULATOR
import tkinter as tk

def click(event):
    current = str(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, current + str(event.widget["text"]))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

entry = tk.Entry(root, font=("Arial", 20), borderwidth=2, relief="ridge", justify="right")
entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

# Button layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', 'C', '+'],
    ['=']
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for btn in row:
        button = tk.Button(frame, text=btn, font=("Arial", 18), relief="ridge")
        button.pack(side="left", expand=True, fill="both")
        
        if btn == "=":
            button.config(command=calculate)
        elif btn == "C":
            button.config(command=clear)
        else:
            button.bind("<Button-1>", click)

root.mainloop()
