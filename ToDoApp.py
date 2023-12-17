#TaSK -1
#TO-DO LIST 
from tkinter import *

root=Tk()
root.title("To Do List")
entry=Entry(root, font=("Arial",20))
entry.grid(row=0, column=0,padx=10, pady=10,sticky="we")
add_task=Button(root, text="Add Task", font=("Arial",16))
add_task.grid(row=0, column=1,pady=10, sticky="we")
list_box=Listbox(root, font=("Arial",20))
list_box.grid(row=1, column=0, columnspan=2,padx=10, pady=10, sticky="nswe")
remove_task= Button(root, text="Remove Task", font=("Arial",16))
remove_task.grid(row=2,column=0,columnspan=2, padx=10, pady=10, sticky="we")
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)


root.mainloop()
