import subprocess
import tkinter as tk
from tkinter import ttk
from tkinter import font


def wifi_speed():
    output = subprocess.check_output("speedtest-cli --simple", shell=True)
    return output.decode("utf-8")

def show_speed():
    speed_label.config(text=wifi_speed())

app = tk.Tk()
app.title("wifi spped test")
app.geometry("400x150")

# Create a custom font
custom_font = font.Font(family="Helvetica", size=20, weight="bold")


# Create a button to initiate the test
speed_label = tk.Label(app, text="Measuring....", font=custom_font)
speed_label.place(relx=0.5, rely=0.5, anchor='center')

test_button = tk.Button(app, text="Test Speed", command=show_speed)
test_button.place(relx=0.5, rely=0.8, anchor="center")

# Add some styling
style = ttk.Style()
style.configure("TButton", background="#2EECC71", foreground="white", font=("Helvetica", 12, "bold"))
style.configure("TLabel", font=("Helvetica", 18, "bold"))


app.mainloop()



print(wifi_speed())    