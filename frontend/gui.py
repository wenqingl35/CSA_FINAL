
import tkinter as tk

def on_click():
    button.destroy()
    label.config(text="Pick How Many!")
    label2.pack(pady=1)
    button2.place(x=180, y=50)
    submitbutton.pack(pady=1)
def submit_entry():
    # Retrieve the text from the Entry widget
    user_input = my_entry.get()
    if user_input[0:2] not in cards or user_input[3:5] not in cards:
        label.config(text="Try Again")
    else:
        cards.remove(user_input[0:2])
        cards.remove(user_input[3:5])
        submit_btn.destroy()
        my_entry.delete(0, tk.END)
def subplay():
    button2.destroy()
    button3.destroy()
    submitbutton.destroy()
    label2.destroy()
    label.config(text="Your Hand!")
    my_entry.pack(pady=10)
    submit_btn.pack()
    
def a():
    button3.place(x=100, y=50)
    i.set(i.get() + 1)
    if i.get() == 5:
        button2.place_forget()
def s():
    button2.place(x=180, y=50)
    i.set(i.get() - 1)
    if i.get() == 1:
        button3.place_forget()
# Create main window
cards = ["as", "ah", "ac", "ad", "2s", "2h", "2c", "2d", "3s", "3h", "3c", "3d", "4s", "4h", "4c", "4d", "5s", "5h", "5c", "5d", "6s", "6h", "6c", "6d", "7s", "7h", "7c", "7d", "8s", "8h", "8c", "8d", "9s", "9h", "9c", "9d", "10s", "10h", "10c", "10d", "js", "jh", "jc", "jd", "qs", "qh", "qc", "qd", "ks", "kh", "kc", "kd"]
root = tk.Tk()
root.title("My App")
root.geometry("300x200")

# Add a label
i = tk.IntVar(value=1)
label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=10)
label2 = tk.Label(root, textvariable=i, font=("Arial", 24))


# Add a button
button = tk.Button(root, text="Start", command=on_click)
button2 = tk.Button(root, text="+", command=a)
button3 = tk.Button(root, text="-", command=s)
submitbutton = tk.Button(root, text="Submit", command=subplay)
button.pack()
my_entry = tk.Entry(root, width=30)
submit_btn = tk.Button(root, text="Submit", command=submit_entry)

# Start the event loop
root.mainloop()