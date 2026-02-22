import random
import tkinter as tk
from tkinter import font, messagebox
import random

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        master.configure(bg="#9400D3")  # Violeta

        self.expression = ""

        self.display = tk.Entry(master, font=("Arial", 20), borderwidth=2, relief="groove", justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        for i, button in enumerate(buttons):
            tk.Button(master, text=button, font=("Arial", 18), bg="#FF69B4", fg="white", command=lambda b=button: self.on_button_click(b)).grid(row=(i//4)+1, column=i%4, padx=5, pady=5)
        
        # Habilitar entrada por teclado
        master.bind('<Key>', self.on_key_press)

    def on_key_press(self, event):
        """Maneja las pulsaciones del teclado"""
        key = event.char
        
        # Números (0-9)
        if key.isdigit() or key in ['+', '-', '*', '/', '.']:
            self.on_button_click(key)
        # Enter para igual
        elif event.keysym == 'Return':
            self.on_button_click('=')
        # Backspace para eliminar último carácter
        elif event.keysym == 'BackSpace':
            self.expression = self.expression[:-1]
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expression)
        # Escape para limpiar todo
        elif event.keysym == 'Escape':
            self.expression = ""
            self.display.delete(0, tk.END)

    def on_button_click(self, char):
        if char == '=':
            try:
                result = eval(self.expression)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
                self.expression = str(result)
            except Exception as e:
                messagebox.showerror("Error", "Invalid Expression")
                self.expression = ""
                self.display.delete(0, tk.END)
        else:
            self.expression += char
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expression)
if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
