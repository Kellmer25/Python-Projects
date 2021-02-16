# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 08:29:15 2021

This is an app, that opens certain websites in order to increase
work flow in the morning.

@author: Anders
"""

import webbrowser as wb
import tkinter as tk

def launch():
    if var[0].get() == 1:
        wb.open_new_tab(url[0].get())
    if var[1].get() == 1:
        wb.open_new_tab(url[1].get())
    if var[2].get() == 1:
        wb.open_new_tab(url[2].get())
    if var[3].get() == 1:
        wb.open_new_tab(url[3].get())
    window.destroy()

window = tk.Tk()
window.title('Uni Starter')

url = [tk.StringVar(value='https://www.moodle.aau.dk/my/'), 
       tk.StringVar(value='https://mail.aau.dk/owa/#path=/mail'), 
       tk.StringVar(value='https://www.overleaf.com/project/601a66d7eebd06e1ebd898a3'), 
       tk.StringVar(value='http://google.co.kr')]

text = [tk.StringVar(value='Moodle'), 
        tk.StringVar(value='AAU Mail'), 
        tk.StringVar(value='Overleaf'), 
        tk.StringVar(value='Google')]

var = [tk.IntVar(value=1), 
       tk.IntVar(value=1), 
       tk.IntVar(value=1), 
       tk.IntVar(value=1)]

index = 0

for x in range(2):
    for y in range(2):
        tk.Checkbutton(window, text=text[index].get(), variable=var[index], onvalue=1, offvalue=0, padx = 5).grid(row=y, column = x, sticky = tk.W)
        index += 1

confirm_button = tk.Button(text='Confirm', command = launch, width=10).grid(row=4, column=1, padx=5, pady=(0,5))
quit_button = tk.Button(text='Quit', command = window.destroy, width=10).grid(row=4, column=0, padx=5, pady=(0,5))

window.mainloop()  