#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 17:17:38 2022

@author: clockshield
"""

from tkinter import *
from PIL import ImageTk, Image
root = Tk()

class CreateElement():
    
    def __init__(self):
        print("This is a CreatElement class")
        
    def createnewElement(self):
        label = Label(root, text = "A new label has just been created using a class", fg = "blue")
        label.pack()
        btn = Button(root, text  = " Button ", command = self.message)
        btn.pack(padx = 20, pady = 20)
        
        
    def message(self):
        messagebox.showinfo("showinfo", "You clicked the button created using the class")
        
create_et= CreateElement()
btn = Button(root, text = "click to create label and button element", command = create_et.createnewElement)
btn.pack(padx = 20, pady = 20)
    
    




root.mainloop()