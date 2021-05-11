from tkinter import *
import tkinter.font as font
import math
from tkinter import ttk
import tkinter as tk


window = tk.Tk()
window.geometry("515x486")
window.title("Számológép")

"""create a notebook"""
notebook = ttk.Notebook(window)
notebook.pack(pady=50, expand=True)
notebook.grid(row=1, column=0)

"""create frames"""
frame0 = ttk.Frame(window)
frame0.grid(row=0, column=0)

frame1 = ttk.Frame(notebook, width=400, height=280)
frame2 = ttk.Frame(notebook, width=400, height=280)

# frame0.pack(fill='both', expand=True)
frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)

"""add frames to notebook"""
notebook.add(frame1, text='Általános')
notebook.add(frame2, text='Tudományos')


e = Entry(frame0, width = 35, borderwidth=5)
e.grid(row=0, column = 0, columnspan = 3,padx = 10, pady=10 )
e.insert(0, "  ")

def button_click(number):
    if(number == 10):
        current = e.get()
        e.delete(0,END)
        e.insert(0, str(current) + ".")

    else:
        current = e.get()
        e.delete(0,END)
        e.insert(0, str(current) + str(number))
    #e.delete(0,END)
    
def button_clear():
    """Function to clear the input field"""
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    f_num = float (first_number)
    e.delete(0, END)
    global muv
    muv = 1  ## 1 = összeadás

def button_equal():
    """Equal function scans the string to evaluates and display it"""
    second_number = e.get()
    e.delete(0,END)
    if muv == 1:
        e.insert(0,f_num + float(second_number))
    elif muv == 2:
        e.insert(0,f_num - float(second_number))
    elif muv == 3:
        e.insert(0,f_num * float(second_number))
    elif muv == 4:
        e.insert(0,f_num / float(second_number))
    elif muv == 5:
        e.insert(0,f_num * float(f_num))
    elif muv == 6:
        e.insert(0,abs (float(f_num)))
    elif muv == 7:
        e.insert(0, -1*(float(f_num)))
    elif muv == 8:
        e.insert (0, f_num % float(second_number))



def button_subtract():
    """subtracts the input value from the current value"""
    first_number = e.get()
    global f_num
    f_num = float(first_number)
    e.delete(0, END)
    global muv
    muv = 2
  
def button_multiply():
    """multiply the current value by the input value"""
    first_number = e.get()
    global f_num
    f_num = float(first_number)
    e.delete(0, END)
    global muv
    muv = 3
    
def button_divide():
    """divide the current value by the input value"""
    first_number = e.get()
    global f_num
    f_num = float(first_number)
    e.delete(0, END)
    global muv
    muv = 4

def button_maradek():
    """Residual division of current value"""
    first_number = e.get()
    global f_num
    f_num = float(first_number)
    e.delete(0, END)
    global muv
    muv = 8

def button_negyzet():
    """We get the square of the current number"""
    first_number = e.get()
    global f_num
    f_num = float(first_number)
    e.delete(0, END)
    global muv
    muv = 5

def button_abszolutertek():
    """Returns the absolute value of the input value"""
    current = e.get()
    e.delete(0,END)
    e.insert(0, abs (float(current)))

def button_minusz():
    """change a positive or negative number"""
    current = e.get()
    e.delete(0,END)
    e.insert(0, -1 * float(current))

def button_recip():
    """Returns the reciprocal of the current value"""
    current = e.get()
    e.delete(0,END)
    e.insert(0, 1 / float(current))

def button_lg():
    """Returns the logarithm of the current value in base ten"""
    current = e.get()
    e.delete(0,END)
    e.insert(0, math.log (float(current),10))

def button_sinus():
    """Returns the sine of the current value"""
    current = e.get()
    e.delete(0,END)
    e.insert(0, math.sin (float(current)))

def button_cos():
    """Returns the cosine of the current value"""
    current = e.get()
    e.delete(0,END)
    e.insert(0, math.cos (float(current)))

def button_ctg():
    """Returns the cotangent of the current value"""
    current = e.get()
    e.delete(0,END)
    e.insert(0, 1/math.tan (float(current)))

def button_tan():
    """Returns the tangent of the current value"""
    current = e.get()
    e.delete(0,END)
    e.insert(0, math.tan (float(current)))

def button_fact():
    """Function to calculate the factorial and display it"""
    current = e.get()
    e.delete(0,END)
    e.insert(0, math.factorial (float(current)))

def button_gyok():
    """Returns the root of the current value"""
    current = e.get()
    e.delete(0,END)
    e.insert(0, math.sqrt (float(current)))
    
def button_undo():
    """Function which works like backspace"""
    length = len(e.get())
    e.delete(length-1, 'end')
    
def button_pipi():
    """Returns the completion of the operation with pi"""
    if e.get() == "0":
        e.delete(0, END)
    length = len(e.get())
    e.insert(length, str(math.pi))
    


"""Create Buttons"""
button_1 = Button(frame1, text = "1" , padx = 40, pady = 20, command =lambda: button_click(1))
button_2 = Button(frame1, text = "2" , padx = 40, pady = 20, command =lambda: button_click(2))
button_3 = Button(frame1, text = "3" , padx = 40, pady = 20, command =lambda: button_click(3))
button_4 = Button(frame1, text = "4" , padx = 40, pady = 20, command =lambda: button_click(4))
button_5 = Button(frame1, text = "5" , padx = 40, pady = 20, command =lambda: button_click(5))
button_6 = Button(frame1, text = "6" , padx = 40, pady = 20, command =lambda: button_click(6))
button_7 = Button(frame1, text = "7" , padx = 40, pady = 20, command =lambda: button_click(7))
button_8 = Button(frame1, text = "8" , padx = 40, pady = 20, command =lambda: button_click(8))
button_9 = Button(frame1, text = "9" , padx = 40, pady = 20, command =lambda: button_click(9))
button_0 = Button(frame1, text = "0" , padx = 40, pady = 20, command =lambda: button_click(0))

button_one = Button(frame2, text = "1" , padx = 40, pady = 20, command =lambda: button_click(1))
button_two = Button(frame2, text = "2" , padx = 40, pady = 20, command =lambda: button_click(2))
button_three = Button(frame2, text = "3" , padx = 40, pady = 20, command =lambda: button_click(3))
button_four = Button(frame2, text = "4" , padx = 40, pady = 20, command =lambda: button_click(4))
button_five = Button(frame2, text = "5" , padx = 40, pady = 20, command =lambda: button_click(5))
button_six = Button(frame2, text = "6" , padx = 40, pady = 20, command =lambda: button_click(6))
button_seven = Button(frame2, text = "7" , padx = 40, pady = 20, command =lambda: button_click(7))
button_eight = Button(frame2, text = "8" , padx = 40, pady = 20, command =lambda: button_click(8))
button_nine = Button(frame2, text = "9" , padx = 40, pady = 20, command =lambda: button_click(9))
button_zero = Button(frame2, text = "0" , padx = 40, pady = 20, command =lambda: button_click(0))
button_c = Button(frame2, text = "C" , padx = 40, pady = 20, command = button_clear)
button_osszeadas = Button(frame2, text = "+", padx = 40, pady = 20, command = button_add )
button_kivonas = Button(frame2, text = "-" , padx = 40, pady = 20, command = button_subtract)
button_szorzas = Button(frame2, text = "*" , padx = 40, pady = 20, command = button_multiply)
button_backspace = Button(frame1, text = "<<", padx = 35, pady = 20,font = 'times 15 bold', command =lambda: button_undo())

button_add = Button(frame1, text = "+" , padx = 40, pady = 20, command = button_add)
button_equal = Button(frame1, text = "=" , padx = 80, pady = 20, command = button_equal)
button_clear = Button(frame1, text = "C" , padx = 80, pady = 20, command = button_clear)
button_subtract = Button(frame1, text = "-" , padx = 40, pady = 20, command = button_subtract)
button_multiply = Button(frame1, text = "*" , padx = 40, pady = 20, command = button_multiply)
button_divide = Button(frame1, text = "/" , padx = 40, pady = 20, command = button_divide)
button_vesszo = Button(frame1, text = ".", padx = 40, pady =20, command =lambda: button_click(10)) # 10 = "."
button_negyzet = Button(frame2, text = "x^2", padx = 30, pady = 20, command = button_negyzet)
button_abszolutertek=Button(frame2, text= "|x|", padx=30,pady=20,command = button_abszolutertek)
button_minusz=Button(frame1,text= "-/+", padx=30,pady=20,command=button_minusz)
button_recip=Button(frame2, text = "1/x", padx = 30,pady = 20, command= button_recip)
button_lg= Button(frame2, text = "lg", padx = 35, pady = 20, command = button_lg)
button_sinus= Button(frame2, text = "sin", padx = 30, pady = 20, command = button_sinus)
button_cos=Button(frame2, text = "cos", padx = 30, pady = 20, command = button_cos)
button_tan=Button(frame2, text = "tan", padx = 30, pady = 20, command = button_tan)
button_ctg=Button(frame2, text = "ctg", padx = 30, pady = 20, command = button_ctg)
button_fact=Button(frame2,text = "n!", padx = 35, pady= 20, command = button_fact)
button_pi = Button(frame1, text = "pi", padx = 35, pady = 20, command = button_pipi)
button_gyok= Button (frame2, text = "sqrt", padx = 25, pady = 20, command = button_gyok)
button_maradekos = Button(frame1, text = "%",padx = 40, pady = 20, command= button_maradek )

"""Create fonts"""
myFont=font.Font(family= 'Courier', size = 12, weight='bold')
button_1['font']=myFont
button_2['font']=myFont
button_3['font']=myFont
button_4['font']=myFont
button_5['font']=myFont
button_6['font']=myFont
button_7['font']=myFont
button_8['font']=myFont
button_9['font']=myFont
button_0['font']=myFont

button_one['font']= myFont
button_two['font']= myFont
button_three['font']= myFont
button_four['font']= myFont
button_five['font']= myFont
button_six['font']= myFont
button_seven['font']= myFont
button_eight['font']= myFont
button_nine['font']= myFont
button_zero['font']= myFont
button_osszeadas['font']=myFont
button_kivonas['font']=myFont
button_szorzas['font']=myFont
button_c['font'] = myFont

button_add['font']=myFont
button_equal['font']=myFont
button_clear['font']=myFont
button_subtract['font']=myFont
button_multiply['font']=myFont
button_divide['font']=myFont
button_vesszo['font']=myFont
button_negyzet['font']=myFont
button_abszolutertek['font']=myFont
button_minusz['font']=myFont
button_recip['font']=myFont
button_lg['font']=myFont
button_sinus['font']=myFont
button_cos['font']=myFont
button_tan['font']=myFont
button_ctg['font']=myFont
button_fact['font']=myFont
button_pi['font']= myFont
button_gyok['font']= myFont
button_backspace['font'] = myFont
button_maradekos['font'] = myFont

"""Location of buttons"""
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1 , column=2)
button_0.grid(row=4, column=1)

button_clear.grid(row=5,column=0,columnspan = 2, sticky=N+S+E+W)
button_add.grid(row=4,column=3)
button_equal.grid(row=5, column=2, columnspan = 2, sticky=N+S+E+W)
button_subtract.grid(row=3, column = 3)
button_multiply.grid(row=2, column = 3)
button_divide.grid(row=1, column = 3)
button_vesszo.grid(row = 4, column = 2)
button_maradekos.grid(row = 2, column = 4, sticky=N+S+E+W)
button_minusz.grid(row=4, column=0)
button_backspace.grid (row = 1, column = 4)

button_one.grid(row = 1, column = 0)
button_two.grid(row = 1, column = 1)
button_three.grid(row = 1, column = 2)
button_four.grid(row = 2, column = 0)
button_five.grid(row = 2, column = 1)
button_six.grid(row = 2, column = 2)
button_seven.grid(row = 3, column = 0)
button_eight.grid(row = 3, column = 1)
button_nine.grid(row = 3, column = 2)
button_zero.grid(row = 4, column = 0)
button_osszeadas.grid(row = 5, column = 0)
button_kivonas.grid(row=6, column = 0)
button_szorzas.grid(row=6,column = 1)
button_lg.grid(row=4,column = 4)
button_sinus.grid(row= 5,column = 4)
button_cos.grid(row = 5, column = 5)
button_tan.grid(row = 6, column = 4)
button_ctg.grid(row = 6, column = 5)
button_fact.grid(row = 4, column = 5)
button_pi.grid (row = 3, column = 4)
button_gyok.grid(row= 2, column = 5)
button_negyzet.grid (row = 5, column = 1)
button_abszolutertek.grid(row=1,column=4)
button_c.grid(row =4 , column=2 )
button_recip.grid(row=3, column = 4)
button_pi.grid(row = 3, column= 4)



window.mainloop()