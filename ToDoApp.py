#TaSK -1
#TO-DO LIST 
from tkinter import *
from tkinter import messagebox

def adding_task():
    task=entry.get()
    if task:
        list_box.insert(END, task)
        entry.delete(0, END)
    else:
        messagebox.showwarning("Warning!", "Please enter a task!")

def removing_task():
    try:
        selected=list_box.curselection()[0]
        list_box.delete(selected)
    except:
        messagebox.showwarning("Warning", "Please select a task to remove!")
    
    
root=Tk()
root.title("To Do List")
root.config(bg="#333333")

entry=Entry(root, font=("Arial", 20), bg="#e5e5e5", fg="#000000")
entry.grid(row=0, column=0, padx=10, pady=10, sticky="we")

add_task=Button(root, text="Add Task", font=("Arial", 16), bg="#e7a236", fg="#000000", command=adding_task)
add_task.grid(row=0, column=1, pady=10, padx=10, sticky="we")

list_box=Listbox(root, font=("Arial", 20), selectmode=SINGLE, bg="#ffffff")
list_box.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nswe")

remove_task= Button(root, text="Remove Task", font=("Arial", 16), bg="#e7a236", fg="#000000", command=removing_task)
remove_task.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="we")

root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)


root.mainloop()

