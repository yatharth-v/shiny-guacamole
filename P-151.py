# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 20:23:05 2021

@author: yatha
"""
from tkinter import *
import random

root=Tk()
root.title("profit or loss ")
root.geometry("500x500")

month = ("january","feburary","march","april","may","june","july","august","september","october","november","december")
profit = (15000,59342,12000,25000,32567,39567,41078,45456,12000,47842,21978,32000)

month_label = Label(root)
month_label.place(relx = 0.5,rely = 0.2,anchor = CENTER)
month_label ["text"] = "Month : "+str(month)

profit_label = Label(root)
profit_label.place(relx = 0.5,rely = 0.3,anchor = CENTER)
profit_label ["text"] = "Profit : "+str(profit)

max_label = Label(root)
min_label = Label(root)

def max_profits() :
    max_profit = max(profit)
    print ("the maximum profit is : "+str(max_profit))
    max_profit_index = profit.index(max_profit)
    print ("the index of the maximum profit is : "+str(max_profit_index))
    max_month = month [max_profit_index]
    print ("the maximum profit is in the month of : "+str(max_month))
    max_label["text"] = "maximum profit of "+str(max_profit)+"was in the month of"+str(max_month)

def min_profits() :
    min_profit = min(profit)
    print ("the minimum profit is : "+str(min_profit))
    min_profit_index = profit.index(min_profit)
    print ("the index of the minimum profit is : "+str(min_profit_index))
    min_month = month [min_profit_index]
    print ("the minimum profit is in the month of : "+str(min_month))
    min_label["text"] = "minimum profit of "+str(min_profit)+"was in the month of"+str(min_month)
    
btn_max = Button(root,text = "show maximum profit",command = max_profits)
btn_max.place(relx = 0.5,rely = 0.4,anchor = CENTER)
max_label.place(relx =0.5,rely=0.5,anchor = CENTER)

btn_min = Button(root,text = "show minimum profit",command = min_profits)
btn_min.place(relx = 0.5,rely = 0.6,anchor = CENTER)
min_label.place(relx =0.5,rely=0.7,anchor = CENTER)
root.mainloop()
    
    