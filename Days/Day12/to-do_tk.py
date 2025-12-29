import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

TASKS_FILE = "tasks.json"  # Save in same folder as script


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📝 To-Do List")
        self.root.geometry("450x500")
        self.root.configure(bg="#f4f4f4")

        self.tasks = []
        self.check_vars = []  # keep track of checkbox states
        self.load_tasks()

        # ----- Input frame -----
        frame_input = tk.Frame(root, bg="#f4f4f4")
        frame_input.pack(fill="x", pady=10)

        self.task_entry = ttk.Entry(frame_input, width=35)
        self.task_entry.pack(side="left", padx=5)
        self.task_entry.bind("<Return>", lambda e: self.add_task())

        ttk.Button(frame_input, text="Add", command=self.add_task).pack(side="left", padx=5)

        # ----- Scrollable tasks frame -----
        canvas = tk.Canvas(root, bg="#f4f4f4", highlightthickness=0)
        scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
        self.scrollable_frame = tk.Frame(canvas, bg="#f4f4f4")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.render_tasks()

    # ---------- Persistence ----------
    def load_tasks(self):
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, "r") as f:
                self.tasks = json.load(f)
        else:
            self.tasks = []

    def save_tasks(self):
        with open(TASKS_FILE, "w") as f:
            json.dump(self.tasks, f, indent=4)

    # ---------- Task Functions ----------
    def add_task(self):
        task_text = self.task_entry.get().strip()
        if not task_text:
            messagebox.showwarning("Warning", "Task cannot be empty.")
            return
        self.tasks.append({"text": task_text, "done": False})
        self.task_entry.delete(0, tk.END)
        self.save_tasks()
        self.render_tasks()

    def toggle_task(self, index):
        self.tasks[index]["done"] = not self.tasks[index]["done"]
        self.save_tasks()
        self.render_tasks()

    def delete_task(self, index):
        del self.tasks[index]
        self.save_tasks()
        self.render_tasks()

    # ---------- UI Rendering ----------
    def render_tasks(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        self.check_vars.clear()

        for idx, task in enumerate(self.tasks):
            frame = tk.Frame(self.scrollable_frame, bg="#ffffff", relief="solid", bd=1)
            frame.pack(fill="x", pady=4, padx=6)

            var = tk.BooleanVar(value=task["done"])
            self.check_vars.append(var)

            cb = ttk.Checkbutton(
                frame,
                variable=var,
                command=lambda i=idx: self.toggle_task(i)
            )
            cb.pack(side="left", padx=5, pady=5)

            text_style = {"font": ("Segoe UI", 10, "overstrike")} if task["done"] else {"font": ("Segoe UI", 10)}
            label = tk.Label(frame, text=task["text"], bg="#ffffff", **text_style)
            label.pack(side="left", fill="x", expand=True, padx=5)

            del_btn = ttk.Button(frame, text="🗑", width=3, command=lambda i=idx: self.delete_task(i))
            del_btn.pack(side="right", padx=5, pady=5)


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
