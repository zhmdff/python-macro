import time
import tkinter as tk
import pyautogui

is_stop = False

def on_button_click():
    global is_stop
    print("input key (00 - lmb, 01 - rmb):", entry1.get())
    print("delay between clicks:", entry2.get())
    print("loop time:", entry3.get())
    
    is_stop = False
    perform_actions()

def perform_actions():
    global is_stop
    time.sleep(3)
    if not is_stop:
        key = entry1.get()
        delay = int(entry2.get())
        loop_time = int(entry3.get())

        if key == "00":
            pyautogui.click()
        elif key == "01":
            pyautogui.click(button='right')
        elif key != "":
            pyautogui.press(key)

        if not is_stop:
            entry1.after(delay, perform_actions)
            loop_time -= 1
            if loop_time <= 0:
                is_stop = True

def on_button_click2():
    global is_stop
    is_stop = True

root = tk.Tk()
root.title("Input Window")

label1 = tk.Label(root, text="input key (00 - lmb, 01 - rmb):")
label1.grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

label2 = tk.Label(root, text="delay between clicks:")
label2.grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

label3 = tk.Label(root, text="loop time:")
label3.grid(row=2, column=0)
entry3 = tk.Entry(root)
entry3.grid(row=2, column=1)

button_submit = tk.Button(root, text="Submit", command=on_button_click)
button_submit.grid(row=3, column=0)

button_stop = tk.Button(root, text="Stop", command=on_button_click2)
button_stop.grid(row=3, column=1)

root.mainloop()
