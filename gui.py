import tkinter

import tkhtmlview
from tkhtmlview import HTMLLabel
class MyApp:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Phone Tracker")
        self.root.configure(background="grey")
        self.root.resizable(width=True, height=True)
        self.root.geometry("1042x521+0+0")


        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        label_text = tkinter.Frame(self.root, background="green", width=700, height=400)
        label_text.grid( column=0, sticky="nesw")

        tkinter.Label(label_text, text="Hello! we will track the phone location",font=("Arial", 25)).grid(row=0, column=0, sticky="nesw")

        country_name = tkinter.StringVar()
        tkinter.Label(label_text, text="Enter Country Name:",font=("Arial", 18)).grid(row = 1, column = 0, sticky=tkinter.W, padx=5, pady=5)

        tkinter.Entry(label_text, textvariable=country_name,font=("Arial", 18)).grid(row = 1, column = 1, sticky=tkinter.E, padx=5, pady=5)

        mo_number = tkinter.StringVar()
        tkinter.Label(label_text, text="Enter your Mobile Number:",font=("Arial", 18)).grid(row = 2, column = 0, sticky=tkinter.W, padx=5, pady=5)
        tkinter.Entry(label_text, textvariable=mo_number,font=("Arial", 18)).grid(row = 2, column = 1, sticky=tkinter.E, padx=5, pady=5)

        label_text2 = tkinter.Frame(self.root, background="black", width=300, height=900)
        label_text2.grid(row=0,column=1, sticky="nesw")


App = MyApp()
App.root.mainloop()