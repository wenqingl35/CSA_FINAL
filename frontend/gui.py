import tkinter as tk
import requests
import json

apiurl = "https://laughing-lamp-974gv5gr5q992777x-8000.app.github.dev"

# -----------------------------
# GLOBAL STATE
# -----------------------------
action_list = []
opponents_list = []
user_input = ""
position_input = ""
action_input = ""
called_or_raised = 0
flop_input = ""
board_num = 0
pot_size_value = 0.0

actions = ["fold", "call", "raise"]
positions = ["CO", "BB", "SB", "UTG", "BTN", "MP"]

cards = [
    "As","Ah","Ac","Ad","2s","2h","2c","2d","3s","3h","3c","3d",
    "4s","4h","4c","4d","5s","5h","5c","5d","6s","6h","6c","6d",
    "7s","7h","7c","7d","8s","8h","8c","8d","9s","9h","9c","9d",
    "10s","10h","10c","10d","Js","Jh","Jc","Jd","Qs","Qh","Qc","Qd",
    "Ks","Kh","Kc","Kd"
]

# -----------------------------
# MAIN WINDOW
# -----------------------------
root = tk.Tk()
root.title("Poker GUI")
root.geometry("350x350")

i = tk.IntVar(value=1)
j = tk.IntVar(value=1)

label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=10)

label2 = tk.Label(root, textvariable=i, font=("Arial", 24))

button = tk.Button(root, text="Start", command=lambda: on_click())
button.pack()

my_entry = tk.Entry(root, width=30)

submit_btn = tk.Button(root, text="Submit", command=lambda: submit_entry())
position_button = tk.Button(root, text="Submit", command=lambda: position())
pot_button = tk.Button(root, text="Submit", command=lambda: pot_size())
action_button = tk.Button(root, text="Submit", command=lambda: action())
call_raise_button = tk.Button(root, text="Submit", command=lambda: call_raise())
flop_button = tk.Button(root, text="Submit", command=lambda: flop())

three_button = tk.Button(root, text="Finish", command=lambda: three_board())
four_button = tk.Button(root, text="Finish", command=lambda: four_board())
five_button = tk.Button(root, text="Finish", command=lambda: five_board())

button2 = tk.Button(root, text="+", command=lambda: add())
button3 = tk.Button(root, text="-", command=lambda: subtract())
submitbutton = tk.Button(root, text="Submit", command=lambda: subplay())

label3 = tk.Label(root, text="")
label4 = tk.Label(root, text="")
label5 = tk.Label(root, text="")
label6 = tk.Label(root, text="")

opponent1 = tk.Entry(root, width=30)
opponent2 = tk.Entry(root, width=30)
opponent3 = tk.Entry(root, width=30)
opponent4 = tk.Entry(root, width=30)

opponent_button = tk.Button(root, text="Submit", command=lambda: opsub())

# -----------------------------
# STEP FUNCTIONS
# -----------------------------

def on_click():
    button.destroy()
    label.config(text="Pick How Many Opponents!")
    label2.pack(pady=1)
    button2.place(x=175 + 40, y=50)
    submitbutton.pack(pady=1)

def subplay():
    button2.destroy()
    button3.destroy()
    submitbutton.destroy()
    label2.destroy()

    label.config(text="Your Hand!")
    my_entry.pack(pady=10)
    submit_btn.pack()

def submit_entry():
    global user_input
    user_input = my_entry.get().strip()

    if len(user_input) < 5:
        label.config(text="Wrong Format!")
        return

    c1 = user_input[0:2]
    c2 = user_input[3:5]

    if c1 not in cards or c2 not in cards:
        label.config(text="Try Again, Wrong Format!")
        return

    if c1 == c2:
        label.config(text="Duplicate Cards!")
        return

    cards.remove(c1)
    cards.remove(c2)

    submit_btn.destroy()
    my_entry.delete(0, tk.END)
    label.config(text="Enter Your Position!")
    position_button.pack(pady=10)

def position():
    global position_input
    position_input = my_entry.get().strip()

    if position_input not in positions:
        label.config(text="Invalid Position!")
        return

    position_button.destroy()
    my_entry.delete(0, tk.END)
    label.config(text="Enter Pot Size!")
    pot_button.pack(pady=10)

def pot_size():
    global pot_size_value
    pot_text = my_entry.get().strip()

    try:
        pot_size_value = float(pot_text)
    except:
        label.config(text="Invalid pot size!")
        return

    pot_button.destroy()
    my_entry.delete(0, tk.END)
    label.config(text="Enter Your Action!")
    action_button.pack(pady=10)

def action():
    global action_input
    action_input = my_entry.get().strip()

    if action_input not in actions:
        label.config(text="Invalid Action!")
        return

    if action_input in ("call", "raise"):
        my_entry.delete(0, tk.END)
        label.config(text=f"Enter {action_input} Amount")
        action_button.destroy()
        call_raise_button.pack(pady=10)
    else:
        action_list.append({
            "player": "Hero",
            "action": action_input,
            "amount": 0
        })
        action_button.destroy()
        my_entry.delete(0, tk.END)
        label.config(text="How Many Cards On Board?")
        flop_button.pack(pady=10)

def call_raise():
    global called_or_raised
    called_or_raised = my_entry.get().strip()

    try:
        amt = int(called_or_raised)
    except:
        label.config(text="Not an integer!")
        return

    action_list.append({
        "player": "Hero",
        "action": action_input,
        "amount": amt
    })

    my_entry.delete(0, tk.END)
    call_raise_button.destroy()
    label.config(text="How Many Cards On Board?")
    flop_button.pack(pady=10)

def flop():
    global board_num
    try:
        board_num = int(my_entry.get().strip())
    except:
        label.config(text="Invalid Number")
        return

    if board_num not in [0, 3, 4, 5]:
        label.config(text="Invalid Number")
        return

    flop_button.destroy()
    my_entry.delete(0, tk.END)

    if board_num == 0:
        opponents_input()
        return

    label.config(text="Enter Board Cards")

    if board_num == 3:
        three_button.pack(pady=10)
    elif board_num == 4:
        four_button.pack(pady=10)
    else:
        five_button.pack(pady=10)

# -----------------------------
# BOARD VALIDATION
# -----------------------------
def parse_board(n):
    global flop_input
    flop_input = my_entry.get().strip()

    parts = flop_input.split()
    if len(parts) != n:
        label.config(text=f"Expected {n} cards separated by spaces.")
        return False

    used = set()
    for c in parts:
        if c not in cards:
            label.config(text=f"Invalid card: {c}")
            return False
        if c in used:
            label.config(text=f"Duplicate card: {c}")
            return False
        used.add(c)

    return True

def three_board():
    if parse_board(3):
        opponents_input()

def four_board():
    if parse_board(4):
        opponents_input()

def five_board():
    if parse_board(5):
        opponents_input()

# -----------------------------
# OPPONENTS
# -----------------------------
def opponents_input():
    my_entry.pack_forget()
    label.config(text="Opponent Info")

    three_button.pack_forget()
    four_button.pack_forget()
    five_button.pack_forget()

    label3.config(text=f"Opponent {j.get()} Name:")
    label4.config(text=f"Opponent {j.get()} Position:")
    label5.config(text=f"Opponent {j.get()} Stack:")
    label6.config(text=f"Opponent {j.get()} Notes:")

    label3.pack(pady=5)
    opponent1.pack(pady=5)
    label4.pack(pady=5)
    opponent2.pack(pady=5)
    label5.pack(pady=5)
    opponent3.pack(pady=5)
    label6.pack(pady=5)
    opponent4.pack(pady=5)
    opponent_button.pack(pady=10)

def opsub():
    name = opponent1.get().strip()
    pos = opponent2.get().strip()
    stack_text = opponent3.get().strip()
    notes = opponent4.get().strip()

    # --- VALIDATION ---

    # Name required
    if name == "":
        label.config(text="Opponent name cannot be empty!")
        return

    # Position must be valid
    if pos not in positions:
        label.config(text="Invalid opponent position!")
        return

    # Stack must be a number
    try:
        stack = float(stack_text)
    except:
        label.config(text="Stack must be a number!")
        return

    # Stack must be positive
    if stack <= 0:
        label.config(text="Stack must be > 0!")
        return

    # Notes can be empty, that's fine

    # --- STORE OPPONENT ---
    opponents_list.append({
        "name": name,
        "position": pos,
        "stack": stack,
        "notes": notes
    })

    # Move to next opponent
    j.set(j.get() + 1)

    if j.get() > i.get():
        finished()
        return

    # Clear fields for next opponent
    opponent1.delete(0, tk.END)
    opponent2.delete(0, tk.END)
    opponent3.delete(0, tk.END)
    opponent4.delete(0, tk.END)

    label3.config(text=f"Opponent {j.get()} Name:")
    label4.config(text=f"Opponent {j.get()} Position:")
    label5.config(text=f"Opponent {j.get()} Stack:")
    label6.config(text=f"Opponent {j.get()} Notes:")

# -----------------------------
# ADD / SUBTRACT (UNCHANGED)
# -----------------------------
def add():
    button3.place(x=175 - 40, y=50)
    i.set(i.get() + 1)
    if i.get() == 5:
        button2.place_forget()
        
def subtract():
    button2.place(x=175 + 40, y=50)
    i.set(i.get() - 1)
    if i.get() == 1:
        button3.place_forget()

# -----------------------------
# FINISHED → API + JSON OUTPUT
# -----------------------------
def finished():
    global action_list, opponents_list, user_input, position_input
    global action_input, called_or_raised, flop_input, board_num, pot_size_value

    # Clear screen
    for widget in root.winfo_children():
        widget.destroy()

    status_label = tk.Label(root, text="Sending to API...", font=("Arial", 16))
    status_label.pack(pady=20)
    root.update()

    # Build payload
    payload = {
        "game_type": "NLHE Cash Game 6-Max",
        "hero_hand": [user_input[0:2], user_input[3:5]],
        "board": flop_input.split() if flop_input else [],
        "hero_position": position_input,
        "hero_stack": float(called_or_raised),
        "pot_size": pot_size_value,
        "action_history": action_list,
        "opponents": opponents_list
    }

    # API calls
    r = requests.post(f"{apiurl}/hand/start", json=payload)
    r2 = requests.get(f"{apiurl}/hand/current")

    # Replace screen with JSON
    status_label.config(text="API Response:")

    frame = tk.Frame(root)
    frame.pack(fill="both", expand=True)

    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side="right", fill="y")

    text_box = tk.Text(
        frame,
        width=60,
        height=20,
        yscrollcommand=scrollbar.set,
        bg="#1e1e1e",
        fg="#ffffff",
        font=("Consolas", 10)
    )
    text_box.pack(side="left", fill="both", expand=True)
    scrollbar.config(command=text_box.yview)

    try:
        formatted = json.dumps(r2.json(), indent=4)
        text_box.insert(tk.END, formatted)
    except:
        text_box.insert(tk.END, "Invalid JSON returned:\n\n" + r2.text)

    # -----------------------------
    # NEW: Update Hand button
    # -----------------------------
    update_button = tk.Button(root, text="Update Hand", font=("Arial", 14),
                            command=lambda: update_board_screen())
    update_button.pack(pady=15)

def update_board_screen():
    for widget in root.winfo_children():
        widget.destroy()

    current_board = flop_input.split() if flop_input else []
    cards_needed = 5 - len(current_board)

    # If board is already complete → skip to actions
    if cards_needed <= 0:
        update_actions_screen()
        return

    title = tk.Label(root, text=f"Add {cards_needed} More Board Card(s)", font=("Arial", 16))
    title.pack(pady=10)

    entry = tk.Entry(root, width=30)
    entry.pack(pady=10)

    def save_board():
        global flop_input
        new_cards = entry.get().strip().split()

        if len(new_cards) != cards_needed:
            title.config(text=f"Enter exactly {cards_needed} card(s)")
            return

        flop_input = " ".join(current_board + new_cards)
        update_actions_screen()

    save_button = tk.Button(root, text="Next", command=save_board)
    save_button.pack(pady=10)

def update_actions_screen():
    for widget in root.winfo_children():
        widget.destroy()

    title = tk.Label(root, text="Update Actions", font=("Arial", 16))
    title.pack(pady=10)

    entry = tk.Entry(root, width=40)
    entry.insert(0, str(action_list))
    entry.pack(pady=10)

    def save_actions():
        global action_list
        try:
            action_list = eval(entry.get().strip())
        except:
            title.config(text="Invalid action format")
            return

        update_pot_screen()

    next_button = tk.Button(root, text="Next", command=save_actions)
    next_button.pack(pady=10)

def update_actions_screen():
    for widget in root.winfo_children():
        widget.destroy()

    title = tk.Label(root, text="Update Actions", font=("Arial", 16))
    title.pack(pady=10)

    entry = tk.Entry(root, width=40)
    entry.insert(0, str(action_list))
    entry.pack(pady=10)

    def save_actions():
        global action_list
        try:
            action_list = eval(entry.get().strip())
        except:
            title.config(text="Invalid action format")
            return

        update_pot_screen()

    next_button = tk.Button(root, text="Next", command=save_actions)
    next_button.pack(pady=10)
    
def update_pot_screen():
    for widget in root.winfo_children():
        widget.destroy()

    title = tk.Label(root, text="Update Pot Size", font=("Arial", 16))
    title.pack(pady=10)

    entry = tk.Entry(root, width=20)
    entry.insert(0, str(pot_size_value))
    entry.pack(pady=10)

    def save_pot():
        global pot_size_value
        try:
            pot_size_value = float(entry.get().strip())
        except:
            title.config(text="Invalid pot size")
            return

        analyze_updated_hand()

    next_button = tk.Button(root, text="Analyze", command=save_pot)
    next_button.pack(pady=10)

def analyze_updated_hand():
    for widget in root.winfo_children():
        widget.destroy()

    # Build update payload
    update_payload = {
        "board": flop_input.split(),
        "actions": action_list
    }

    # Send update
    requests.post(f"{apiurl}/hand/update", json=update_payload)

    # Get analysis
    analysis = requests.get(f"{apiurl}/hand/current").json()

    title = tk.Label(root, text="Updated Analysis", font=("Arial", 16))
    title.pack(pady=10)

    frame = tk.Frame(root)
    frame.pack(fill="both", expand=True)

    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side="right", fill="y")

    text_box = tk.Text(
        frame,
        width=60,
        height=20,
        yscrollcommand=scrollbar.set,
        bg="#1e1e1e",
        fg="#ffffff",
        font=("Consolas", 10)
    )
    text_box.pack(side="left", fill="both", expand=True)
    scrollbar.config(command=text_box.yview)

    text_box.insert(tk.END, json.dumps(analysis, indent=4))

root.mainloop()