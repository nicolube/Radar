from serial import Serial
from serial.tools.list_ports import comports
import serial
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk, themed_tk


ser = Serial

class App(ThemedTk):
    def __init__(self):
        super().__init__()
        # root window
        self.title('Theme Demo')
        self.geometry('400x300')
        self.style = ttk.Style(self)

        # radio button
        self.selected_theme = tk.StringVar()
        theme_frame = ttk.LabelFrame(self, text='Themes')
        theme_frame.grid(padx=10, pady=10, ipadx=20, ipady=20, sticky='w')

        serialPortNames = [comp.name for comp in comports()]
        variable = tk.StringVar(self)
        variable.set(serialPortNames[0])
        opt = tk.OptionMenu(theme_frame, variable, *serialPortNames)
        opt.config(width=90, font=('Helvetica', 12))
        opt.pack()
    
        for theme_name in self.style.theme_names():
            print(theme_name)
            rb = ttk.Radiobutton(
                theme_frame,
                text=theme_name,
                value=theme_name,
                variable=self.selected_theme,
                command=self.updateTheme
                )
            rb.pack(expand=True, fill='both')
        self.style.theme_use("scidgrey")
        
    def updateTheme(self):
        self.style.theme_use(self.selected_theme.get())

if __name__ == "__main__":
    app = App()
    app.mainloop()