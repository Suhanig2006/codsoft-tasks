# TO DO LIST
import tkinter as tk
from tkinter import messagebox, filedialog
from datetime import datetime

PRIORITY_COLORS = {
    "High": "#f38989",     # Light red
    "Medium": "#73cbf1",   # Light blue
    "Low": "#7fee7f"       # Light green
}

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("My To-Do List")
        self.root.geometry("550x620")
        self.root.configure(bg="#eee83c")

        self.tasks = []

        # Title
        tk.Label(root, text="✨ My To-Do List", font=("Helvetica", 20, "bold"), bg="#8080ea", fg="#333").pack(pady=10)

        # Entry Frame
        entry_frame = tk.Frame(root, bg="#f2f56a")
        entry_frame.pack(pady=10)

        tk.Label(entry_frame, text="Task:", bg="#f0f0f5", font=("Arial", 11)).grid(row=0, column=0, padx=5, sticky="e")
        self.task_entry = tk.Entry(entry_frame, width=30, font=("Arial", 11))
        self.task_entry.grid(row=0, column=1, padx=5)

        tk.Label(entry_frame, text="Due Date (DD-MM-YYYY):", bg="#f0f0f5", font=("Arial", 11)).grid(row=1, column=0, padx=5, sticky="e")
        self.date_entry = tk.Entry(entry_frame, width=30, font=("Arial", 11))
        self.date_entry.grid(row=1, column=1, padx=5)

        tk.Label(entry_frame, text="Priority:", bg="#f0f0f5", font=("Arial", 11)).grid(row=2, column=0, padx=5, sticky="e")
        self.priority_var = tk.StringVar()
        self.priority_var.set("Medium")
        tk.OptionMenu(entry_frame, self.priority_var, "High", "Medium", "Low").grid(row=2, column=1, sticky="w")

        tk.Button(entry_frame, text="➕ Add Task", command=self.add_task, bg="#53D757", fg="black", font=("Arial", 11, "bold")).grid(row=3, column=1, pady=10)

        # Task Display Frame
        self.task_frame = tk.Frame(root, bg="orange", bd=2, relief=tk.GROOVE)
        self.task_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        canvas = tk.Canvas(self.task_frame, bg="white")
        scrollbar = tk.Scrollbar(self.task_frame, orient="vertical", command=canvas.yview)
        self.task_list = tk.Frame(canvas,bg="#f0f8ff")

        self.task_list.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=self.task_list, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Buttons
        button_frame = tk.Frame(root, bg="#b4a5e8")
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="✅ Delete Completed", command=self.delete_completed, bg="#ed71b8", fg="black", width=18).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(button_frame, text="🧹 Clear All", command=self.clear_all, bg="#E2A5ED", fg="black", width=18).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(button_frame, text="💾 Save", command=self.save_tasks, bg="#2196F3", fg="black", width=18).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(button_frame, text="📂 Load", command=self.load_tasks, bg="#77E075", fg="black", width=18).grid(row=1, column=1, padx=5, pady=5)

    def add_task(self):
        task_text = self.task_entry.get().strip()
        due_date = self.date_entry.get().strip()
        priority = self.priority_var.get()

        if not task_text:
            messagebox.showwarning("Input Error", "Please enter a task.")
            return

        if due_date:
            try:
                datetime.strptime(due_date, "%d-%m-%Y")
            except ValueError:
                messagebox.showerror("Date Format Error", "Use DD-MM-YYYY format.")
                return

        var = tk.IntVar()
        full_text = f"{task_text} | Due: {due_date or 'N/A'} | Priority: {priority}"

        cb_frame = tk.Frame(self.task_list, bg=PRIORITY_COLORS[priority], pady=3)
        cb = tk.Checkbutton(cb_frame, text=full_text, variable=var,
                            font=("Arial", 11), anchor="w", bg=PRIORITY_COLORS[priority],
                            activebackground=PRIORITY_COLORS[priority], wraplength=450, justify="left")
        cb.pack(fill="x", padx=10)
        cb_frame.pack(fill="x", padx=5, pady=3)

        self.tasks.append((cb_frame, cb, var))

        self.task_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.priority_var.set("Medium")

    def delete_completed(self):
        for cb_frame, cb, var in self.tasks[:]:
            if var.get() == 1:
                cb_frame.destroy()
                self.tasks.remove((cb_frame, cb, var))

    def clear_all(self):
        if messagebox.askyesno("Clear All", "Are you sure you want to delete all tasks?"):
            for cb_frame, cb, var in self.tasks:
                cb_frame.destroy()
            self.tasks.clear()

    def save_tasks(self):
        path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if not path: return
        with open(path, "w") as f:
            for cb_frame, cb, var in self.tasks:
                f.write(f"{cb.cget('text')}||{var.get()}\n")
        messagebox.showinfo("Saved", "Tasks saved!")

    def load_tasks(self):
        path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if not path: return
        for cb_frame, cb, var in self.tasks:
            cb_frame.destroy()
        self.tasks.clear()

        with open(path, "r") as f:
            for line in f:
                if "||" in line:
                    text, status = line.strip().split("||")
                    priority = "Medium"
                    for p in PRIORITY_COLORS:
                        if f"Priority: {p}" in text:
                            priority = p
                            break
                    var = tk.IntVar(value=int(status))
                    cb_frame = tk.Frame(self.task_list, bg=PRIORITY_COLORS[priority], pady=3)
                    cb = tk.Checkbutton(cb_frame, text=text, variable=var,
                                        font=("Arial", 11), anchor="w", bg=PRIORITY_COLORS[priority],
                                        activebackground=PRIORITY_COLORS[priority], wraplength=450, justify="left")
                    cb.pack(fill="x", padx=10)
                    cb_frame.pack(fill="x", padx=5, pady=3)
                    self.tasks.append((cb_frame, cb, var))
        messagebox.showinfo("Loaded", "Tasks loaded!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
