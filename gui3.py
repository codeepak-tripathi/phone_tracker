import math
import tkinter.messagebox
from tkinter import *
import tkhtmlview

root = Tk()
root.title("Calculator")
root.configure(background="lightgray")
root.resizable(width=True,height=True)
root.geometry("1042x521+0+0")

root.grid_columnconfigure(0, weight = 1)
root.grid_columnconfigure(1, weight = 1)
root.grid_rowconfigure(0, weight = 1)

calc = Frame(root, bg = "red")
calc.grid(row = 0, column = 0, sticky = "nesw")
HtmlFile = open("myLoc.html", 'r', encoding='utf-8')
source_code = HtmlFile.read()
print(source_code)
tkhtmlview.HTMLLabel(root, html=HtmlFile).grid(row = 0, column = 0)

history = Frame(root, bg = "green")
history.grid(row = 0, column = 1, sticky = "nesw")

root.mainloop()
