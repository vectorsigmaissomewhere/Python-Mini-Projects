import tkinter as tk
from tkinter import * 
from tkinter.ttk import * 
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()

def save_task(text_widget):
    task_text = text_widget.get("1.0", tk.END).strip()  # Get text from input field
    if task_text:  # Only save if text is not empty
        with open("tasks.txt", "a") as file:
            file.write(task_text + "\n")  # Append task to the file
        text_widget.delete("1.0", tk.END)  # Clear the text field
        print("Task saved successfully!")

def button_clicked():
    new_window = Toplevel(root)
    new_window.title("Add Task")
    new_window.geometry("500x450")

    label = tk.Label(new_window, text="Add Task", font=("Arial", 14, "bold"))
    label.pack(pady=10)

    text_field = tk.Text(new_window, height=5, width=50)
    text_field.pack(pady=10)

    add_button = tk.Button(new_window, text="Save Task", command=lambda: save_task(text_field))
    add_button.pack(pady=5)

    print("Button Clicked")

def view_task():
    view_window = tk.Toplevel(root)

    # Read tasks from file
    somelists = []
    with open("tasks.txt", 'r') as f:
        somelists = [line.strip() for line in f]

    # Create a Treeview widget
    tree = ttk.Treeview(view_window, columns=("Task"), show="headings", height=len(somelists))
    tree.heading("Task", text="Tasks")

    # Insert data into the Treeview
    for task in somelists:
        tree.insert("", "end", values=(task,))

    tree.pack(padx=10, pady=10)

    def delete_task():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a task to delete.")
            return

        task_to_delete = tree.item(selected_item, "values")[0]
        tree.delete(selected_item)

        # Update tasks in file
        with open("tasks.txt", 'w') as f:
            for task in somelists:
                if task != task_to_delete:
                    f.write(task + "\n")

        messagebox.showinfo("Deleted", f"Task '{task_to_delete}' deleted successfully.")

    def update_task():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a task to update.")
            return

        task_to_update = tree.item(selected_item, "values")[0]
        
        # Create a pop-up window to edit the task
        def save_updated_task():
            updated_task = update_entry.get()
            if updated_task:
                # Update the task in the Treeview
                tree.item(selected_item, values=(updated_task,))
                
                # Update the task in the list
                index = somelists.index(task_to_update)
                somelists[index] = updated_task
                
                # Update tasks in the file
                with open("tasks.txt", 'w') as f:
                    for task in somelists:
                        f.write(task + "\n")
                
                messagebox.showinfo("Updated", f"Task updated to '{updated_task}'.")
                update_window.destroy()
            else:
                messagebox.showwarning("Warning", "Task cannot be empty.")

        # Create the update window
        update_window = tk.Toplevel(view_window)
        update_window.title("Update Task")
        update_window.geometry("300x150")

        # Create input field and save button
        update_label = tk.Label(update_window, text="Edit Task:")
        update_label.pack(pady=10)
        
        update_entry = tk.Entry(update_window, width=30)
        update_entry.insert(0, task_to_update)
        update_entry.pack(pady=5)

        save_button = tk.Button(update_window, text="Save", command=save_updated_task)
        save_button.pack(pady=10)

    update_btn = tk.Button(view_window, text="Update Task", command=update_task, bg="yellow", fg="black")
    update_btn.pack(pady=10)

    delete_btn = tk.Button(view_window, text="Delete Task", command=delete_task, bg="red", fg="white")
    delete_btn.pack(pady=10)

    view_window.title("View Task")
    view_window.geometry("500x450")

root.title("Welcome to the Game")
root.geometry('500x450')
app_front_text = tk.StringVar()  
app_front_text.set("Todo List App")

label = tk.Label(root, textvariable=app_front_text, anchor=tk.CENTER, bg='lightblue', height=3, width=30, 
                 bd=3, font=("Arial", 16, "bold"), cursor="hand2", fg="red", padx=15, pady=15, 
                 justify=tk.CENTER, relief=tk.RAISED, underline=0, wraplength=250)



label.pack(pady=20)  
addtask_button = tk.Button(root, 
                   text="Add Task", 
                   command=button_clicked,
                   activebackground="blue", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100)

addtask_button.pack(padx=20, pady=20)

viewtask_button = tk.Button(root, 
                   text="View Task", 
                   command=view_task,
                   activebackground="blue", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100)

viewtask_button.pack(padx=20, pady=20)

root.resizable(False, False)
root.mainloop()
