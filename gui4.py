# Import Module
from tkinter import *
from tkinterhtml import HtmlFrame
import urllib.request

import tkhtmlview
from tkhtmlview import HTMLLabel

# Create Object
root = Tk()

# Set Geometry
root.geometry("900x600")

# Add label
HtmlFile = open("myLoc.html", 'r', encoding='utf-8')
source_code = HtmlFile.read()
frame = HtmlFrame(root, horizontal_scrollbar="auto")
"""my_label = HTMLLabel(root, html=
"""
# Adjust label
#frame = HtmlFrame(root, horizontal_scrollbar="auto")
#, html=source_code
frame.set_content(source_code).decode()

frame.pack()

# Execute Tkinter
root.mainloop()
