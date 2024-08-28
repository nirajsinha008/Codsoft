#import library
from tkinter import *
from tkinter import messagebox

#new task function
def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")

def deleteTask():
    lb.delete(ANCHOR)

#edit tast function
def editTask():
    try:
        selected_task_index = lb.curselection()[0]
        new_task = my_entry.get()
        if new_task != "":
            lb.delete(selected_task_index)
            lb.insert(selected_task_index, new_task)
            my_entry.delete(0, "end")
        else:
            messagebox.showwarning("Warning", "Please enter some task.")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to edit.")
    
# Function to mark the task as completed
def completeTask():
    try:
        selected_task_index = lb.curselection()[0]
        task = lb.get(selected_task_index)
        completed_task = f"{task} (Done)"
        lb.delete(selected_task_index)
        lb.insert(selected_task_index, completed_task)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as completed.")


ws = Tk()
ws.geometry('500x450+500+200')
ws.title('To Do list')
ws.config(bg='#223441')
ws.resizable(width=False, height=False)

frame = Frame(ws)
frame.pack(pady=10)

lb = Listbox(
    frame,
    width=25,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
    
)
lb.pack(side=LEFT, fill=BOTH)

task_list = [
    'Eat apple',
    'drink water',
    'go gym',
    'write software',
    'write documentation',
    'take a nap',
    'Learn something',
    'paint canvas'
    ]

for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    ws,
    font=('times', 24)
    )

my_entry.pack(pady=20)

button_frame = Frame(ws)
button_frame.pack(pady=20)

#add task button
addTask_btn = Button(
    button_frame,
    text='Create',
    font=('times 14'),
    bg='#c5f776',
    padx=20,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

#delete task button
delTask_btn = Button(
    button_frame,
    text='Remove',
    font=('times 14'),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

#edit tast Button
editTask_btn = Button(
    button_frame,
    text='Edit',
    font=('Times', 14),
    bg='#61bfff',
    padx=20,
    pady=10,
    command=editTask
)
editTask_btn.pack(fill=BOTH, expand=True, side=LEFT)
#complete tast Button
completeTask_btn = Button(
    button_frame,
    text='Complete',
    font=('Times', 14),
    bg='#76f7c5',
    padx=20,
    pady=10,
    command=completeTask
)
completeTask_btn.pack(fill=BOTH, expand=True, side=LEFT)


ws.mainloop()