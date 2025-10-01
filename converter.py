# Program Name: converter.py 
# Course: IT3883/Section W02
# Student Name: Anthony Giso
# Assignment Number: 3
# Due Date: 10/03/ 2025
# Purpose: GUI application to convert Miles per Gallon into Kilometers per Liter.  
# Used Python module and chapters.


import tkinter as tk

# Conversion factor
MPG_TO_KPL = 0.425143707

def convert(*args):
    """Convert MPG to Km/L as user types."""
    try:
        mpg = float(mpg_entry.get())
        kpl = mpg * MPG_TO_KPL
        result_var.set(f"{kpl:.3f} Km/L")
    except ValueError:
        # If input is invalid (letters, empty, etc.), clear result
        result_var.set("")

# Create main window
root = tk.Tk()
root.title("MPG to Km/L Converter")

# Input label
tk.Label(root, text="Miles per Gallon (MPG):").grid(row=0, column=0, padx=10, pady=10)

# Input box
mpg_entry = tk.Entry(root)
mpg_entry.grid(row=0, column=1, padx=10, pady=10)
mpg_entry.bind("<KeyRelease>", convert)  # Update result on every key press

# Result label
tk.Label(root, text="Kilometers per Liter (Km/L):").grid(row=1, column=0, padx=10, pady=10)

# Result display
result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=("Arial", 12, "bold"))
result_label.grid(row=1, column=1, padx=10, pady=10)

# Run the application
root.mainloop()
