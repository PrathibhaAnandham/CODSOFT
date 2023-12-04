import tkinter as tk
from tkinter import font
def plus_cal():
    num1 = entry1.get()
    num2= entry2.get()
    res=int(num1)+int(num2)
    label3.config(text=f"Result:{res}")
def sub_cal():
    num1 = entry1.get()
    num2= entry2.get()
    res=int(num1)-int(num2)
    
def mul_cal():
    num1 = entry1.get()
    num2= entry2.get()
    res=int(num1)*int(num2)
    label3.config(text=f"Result:{res}")
def div_cal():
    num1 = entry1.get()
    num2= entry2.get()
    res=int(num1)/int(num2)
    label3.config(text=f"Result:{res}")
def mod_cal():
    num1 = entry1.get()
    num2= entry2.get()
    res=int(num1)%int(num2)
    label3.config(text=f"Result:{res}")
def floordiv_cal():
    num1 = entry1.get()
    num2= entry2.get()
    res=int(num1)//int(num2)
    label3.config(text=f"Result:{res}")
    
def dot_cal():
    num1 = entry1.get()
    num2= entry2.get()
    res=str(num1)+"."+str(num2)
    

    

def number_click(number):
    if entry1.focus_get() == entry1:
        current1 = entry1.get()
        entry1.delete(0, tk.END)
        entry1.insert(tk.END, current1 + str(number))
    elif entry2.focus_get() == entry2:
        current2 = entry2.get()
        entry2.delete(0, tk.END)
        entry2.insert(tk.END, current2 + str(number))

def clear_entry():
    entry1.delete(0, tk.END)


window = tk.Tk()
window.geometry("450x500")
window.config(bg="light gray")
label1 = tk.Label(window, text="Number 1:",bg="light gray")
label1.grid(row=0, column=0)

label2 = tk.Label(window, text="Number 2:",bg="light gray")
label2.grid(row=1, column=0)
label3 = tk.Label(window, text="Result:",bg="light gray")
label3.grid(row=2, column=0)

entry1 = tk.Entry(window)
entry1.grid(row=0, column=1)

entry2 = tk.Entry(window)
entry2.grid(row=1, column=1)
button_font = font.Font(size=30)
button_numbers = []
for i in range(10):
    button_numbers.append(tk.Button(window, text=str(i), width=4, height=1, font=button_font, command=lambda i=i: number_click(i), bg="white", fg="black"))
    button_numbers[i].grid(row=(9-(i-1)//3), column=((i-1)%3), padx=0, pady=0)

button_clear = tk.Button(window, text="C", width=4, height=1, font=button_font, command=clear_entry)
button_clear.grid(row=6, column=0, padx=0, pady=0)

plus = tk.Button(window, text="+", width=4, height=1, font=button_font, command=plus_cal)
plus.grid(row=9, column=4, columnspan=1, padx=0, pady=0)

sub = tk.Button(window, text="-", width=4, height=1, font=button_font, command=sub_cal)
sub.grid(row=8, column=4, columnspan=1, padx=0, pady=0)

mul = tk.Button(window, text="*", width=4, height=1, font=button_font, command=mul_cal)
mul.grid(row=7, column=4, columnspan=1, padx=0, pady=0)

div = tk.Button(window, text="/", width=4, height=1, font=button_font, command=div_cal)
div.grid(row=6, column=4, columnspan=1, padx=0, pady=0)

mod = tk.Button(window, text="%", width=4, height=1, font=button_font, command=mod_cal)
mod.grid(row=6, column=1, columnspan=1, padx=0, pady=0)

floordiv = tk.Button(window, text="//", width=4, height=1, font=button_font, command=floordiv_cal)
floordiv.grid(row=6, column=2, columnspan=1, padx=0, pady=0)

dot = tk.Button(window, text=".", width=4, height=1, font=button_font, command=dot_cal)
dot.grid(row=10, column=0, columnspan=1, padx=0, pady=0)

equal = tk.Button(window, text="=", width=4, height=1, font=button_font)
equal.grid(row=10, column=4, columnspan=1, padx=10, pady=0)

cross = tk.Button(window, text="x", width=4, height=1, font=button_font)
cross.grid(row=10, column=2, columnspan=1, padx=0, pady=0)

doublezero = tk.Button(window, text="00", width=4, height=1, font=button_font)
doublezero.grid(row=10, column=1, columnspan=1, padx=0, pady=0)
~
~window.mainloop()