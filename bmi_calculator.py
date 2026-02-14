import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            messagebox.showerror("Invalid Input", "Please enter positive values!")
            return

        bmi = round(weight / (height ** 2), 2)

        if bmi < 18.5:
            category = "Underweight"
            color = "blue"
        elif 18.5 <= bmi < 25:
            category = "Normal"
            color = "green"
        elif 25 <= bmi < 30:
            category = "Overweight"
            color = "orange"
        else:
            category = "Obese"
            color = "red"

        result_label.config(text=f"BMI: {bmi} ({category})", fg=color)

        with open("bmi_records.txt", "a") as file:
            file.write(f"Weight: {weight}, Height: {height}, BMI: {bmi}, Category: {category}\n")

    except ValueError:
        messagebox.showerror("Invalid Input", "Only numbers are allowed!")

def clear_fields():
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    result_label.config(text="")

root = tk.Tk()
root.title("BMI Calculator")
root.geometry("380x450")
root.resizable(False, False)
root.configure(bg="pink")

title_label = tk.Label(
    root,
    text="BMI Calculator",
    font=("Helvetica", 24, "bold"),
    bg="red",
    fg="white"
)
title_label.pack(pady=25)

weight_label = tk.Label(
    root,
    text="Weight (kg)",
    font=("Arial", 12),
    bg="pink",
    fg="black"
)
weight_label.pack(pady=(10, 0))

weight_entry = tk.Entry(
    root,
    font=("Arial", 14),
    justify="center",
    bg="white",
    fg="black",
    bd=2
)
weight_entry.pack(ipady=8, ipadx=8, pady=5)

height_label = tk.Label(
    root,
    text="Height (meters)",
    font=("Arial", 12),
    bg="pink",
    fg="black"
)
height_label.pack(pady=(10, 0))

height_entry = tk.Entry(
    root,
    font=("Arial", 14),
    justify="center",
    bg="white",
    fg="black",
    bd=2
)
height_entry.pack(ipady=8, ipadx=8, pady=5)

button_frame = tk.Frame(root, bg="pink")
button_frame.pack(pady=20)

calculate_btn = tk.Button(
    button_frame,
    text="Calculate",
    font=("Arial", 12, "bold"),
    bg="green",
    fg="white",
    width=12,
    command=calculate_bmi
)
calculate_btn.grid(row=0, column=0, padx=10)

clear_btn = tk.Button(
    button_frame,
    text="Clear",
    font=("Arial", 12, "bold"),
    bg="blue",
    fg="white",
    width=12,
    command=clear_fields
)
clear_btn.grid(row=0, column=1, padx=10)

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 16, "bold"),
    bg="pink",
    fg="blue"
)
result_label.pack(pady=20)

footer_label = tk.Label(
    root,
    text="Stay Healthy!",
    font=("Helvetica", 12, "italic"),
    bg="pink",
    fg="purple"
)
footer_label.pack(side="bottom", pady=15)

root.mainloop()
