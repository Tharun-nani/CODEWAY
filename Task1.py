import tkinter as tk
class TodoListApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("To-Do List App")
        self.tasks = []
        self.task_entry = tk.Entry(self)
        self.task_entry.pack()
        self.add_button = tk.Button(self, text="Add Task", command=self.add_task)
        self.add_button.pack()
        self.task_listbox = tk.Listbox(self)
        self.task_listbox.pack()
        self.refresh_list()
    def add_task(self):
        task = self.task_entry.get()
        self.tasks.append(task)
        self.refresh_list()
        self.task_entry.delete(0, tk.END)
    def refresh_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)
if __name__ == "__main__":
    app = TodoListApp()
    app.mainloop()
