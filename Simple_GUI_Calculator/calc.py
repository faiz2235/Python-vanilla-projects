import tkinter as tk

def calculate():
    expression = expression_entry.get()
    try:
        result = eval(expression)
        result_label.config(text=f"Result: {result}")
    except:
        result_label.config(text="Invalid expression.")

root = tk.Tk()

expression_label = tk.Label(root, text="Enter expression:")
expression_label.pack()

expression_entry = tk.Entry(root)
expression_entry.pack()

button = tk.Button(root, text="Calculate", command=calculate)
button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
