from tkinter import *
import tkinter.font as font
import math
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox



window = tk.Tk()
window.geometry("535x542")
window.title("Számológép")

"""Create a notebook"""
notebook = ttk.Notebook(window)
notebook.pack(pady=50, expand=True)
notebook.grid(row=1, column=0)

"""Create frames"""
frame0 = ttk.Frame(window)
frame0.grid(row=0, column=0)

frame1 = ttk.Frame(notebook, width=400, height=280)
frame2 = ttk.Frame(notebook, width=400, height=280)
frame3 = ttk.Frame(notebook,width=400, height=280)
frame4 = ttk.Frame(notebook,width=400, height=280)

# frame0.pack(fill='both', expand=True)
frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)
frame3.pack(fill='both', expand=True)
frame4.pack(fill='both', expand=True)

"""add frames to notebook"""
notebook.add(frame1, text='Általános')
notebook.add(frame2, text='Tudományos')
notebook.add(frame3, text='Dátumszámítás')
notebook.add(frame4, text='Hossz átváltás')

"""Adding the input field"""
e = Entry(frame0, width = 50, borderwidth=10)
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

def button_clear1():
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

def button_equal1():
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

def button_divide1():
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

def button_negyzet1():
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

def button_minusz1():
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
    if length == 1:
        e.insert(0,"0")

def button_pipi():
    """Returns the completion of the operation with pi"""
    if e.get() == "0":
        e.delete(0, END)
    length = len(e.get())
    e.insert(length, str(math.pi))

def button_2pipi():
    """Returns the completion of the operation with pi"""
    if e.get() == "0":
        e.delete(0, END)
    length = len(e.get())
    e.insert(length, str(math.tau))

def converter():
    """Calculate conversion from metres"""
    km = float(ent1.get()) / 1000
    mm = float(ent1.get()) * 1000
    cm = float(ent1.get()) * 100
    mf = float(ent1.get()) * 0.00062
    yard = float(ent1.get()) * 1.094
    inch = float(ent1.get()) * 39.37
    lab = float(ent1.get()) * 3.281
    
    text1.delete("1.0", END)
    text1.insert(END, km)

    text2.delete("1.0", END)
    text2.insert(END, mm)

    text3.delete("1.0", END)
    text3.insert(END, cm)

    text4.delete("1.0", END)
    text4.insert(END, mf)

    text5.delete("1.0", END)
    text5.insert(END, yard)

    text6.delete("1.0", END)
    text6.insert(END, inch)

    text7.delete("1.0", END)
    text7.insert(END, lab)

"""Creating Label widgets"""
ent1= StringVar()
label1 = Label(frame4, text="Hossz méterben").grid(row=0, column=0)
ent= Entry(frame4, borderwidth=5, textvariable=ent1).grid(row=0, column=1)
label3 = Label(frame4, text='kilóméter').grid(row=4, column=0)
label4 = Label(frame4, text='miliméter').grid(row=2, column=0)
lable5 = Label(frame4, text='centiméter').grid(row=3, column=0)
label6 = Label(frame4, text='mérföld').grid(row=2, column=2)
label7 = Label(frame4, text='yard').grid(row=4, column=2)
label8 = Label(frame4, text='inch').grid(row=3, column=2)
label9 = Label(frame4, text='láb').grid(row=5, column=0)

text1 = Text(frame4, height=1, width=15, borderwidth=5)
text2 = Text(frame4, height=1, width=15, borderwidth=5)
text3 = Text(frame4, height=1, width=15, borderwidth=5)
text4 = Text(frame4, height=1, width=15, borderwidth=5)
text5 = Text(frame4, height=1, width=15, borderwidth=5)
text6 = Text(frame4, height=1, width=15, borderwidth=5)
text7 = Text(frame4, height=1, width=15, borderwidth=5)

atvalt = Button(frame4, text="Átváltás", command=converter)
atvalt.grid(row=1, column=1)

text1.grid(row=4, column=1)
text2.grid(row=2, column=1)
text3.grid(row=3, column=1)
text4.grid(row=2, column=3)
text5.grid(row=4, column=3)
text6.grid(row=3, column=3)
text7.grid(row=5, column=1)

def clearAll():
    day_field.delete(0, END)
    month_field.delete(0, END)
    year_field.delete(0, END)
    given_day_field.delete(0, END)
    given_month_field.delete(0, END)
    given_year_field.delete(0, END)
    outcome_day.delete(0, END)
    outcome_month.delete(0, END)
    outcome_year.delete(0, END)

def Error():
    """If a field is left blank"""
    if (day_field.get() == "" or month_field.get() == ""
            or year_field.get() == "" or given_day_field.get() == ""
            or given_month_field.get() == "" or given_year_field.get() == ""):
        
        messagebox.showerror("Error", "Some field is empty")
        clearAll()
        return -1

def calculateDate():
    """Date calculation"""
    value = Error()
    if value == -1:
        return

    else:
        dk_day = int(day_field.get())
        dk_month = int(month_field.get())
        dk_year = int(year_field.get())

        given_day = int(given_day_field.get())
        given_month = int(given_month_field.get())
        given_year = int(given_year_field.get())

        month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if (dk_day > given_day):
            given_month = given_month - 1
            given_day = given_day + month[dk_month - 1]

        if (dk_month > given_month):
            given_year = given_year - 1
            given_month = given_month + 12

        calculated_day = given_day - dk_day
        calculated_month = given_month - dk_month
        calculated_year = given_year - dk_year

        outcome_day.insert(10, str(calculated_day))
        outcome_month.insert(10, str(calculated_month))
        outcome_year.insert(10, str(calculated_year))

"""Creating Label widgets"""
start_date= Label(frame3, text="Dátum kezdete").grid(row=0, column=1)
given_date= Label(frame3, text="Dátum vége").grid(row=0, column=4)
nap= Label(frame3, text="Nap").grid(row=1, column=0)
honap = Label(frame3, text="Hónap").grid(row=2, column=0)
ev = Label(frame3, text="Év").grid(row=3, column=0)
given_day = Label(frame3, text="Megadott nap").grid(row=1, column=3)
given_month = Label(frame3, text="Megadott hónap").grid(row=2, column=3)
given_year = Label(frame3, text="Megadott év").grid(row=3, column=3)
outcome_year = Label(frame3, text="Év").grid(row=6, column=0)
outcome_month = Label(frame3, text="Hónap").grid(row=8, column=0)
outcome_day = Label(frame3, text="Nap").grid(row=10, column=0)
outcome_age = Button(frame3, text="Különbség", command=calculateDate).grid(row=4, column=1)
torles = Button(frame3, text="Törlés", command=clearAll).grid(row=12, column=1)

day_field = Entry(frame3, borderwidth=5)
month_field = Entry(frame3, borderwidth=5)
year_field = Entry(frame3, borderwidth=5)

given_day_field = Entry(frame3, borderwidth=5)
given_month_field = Entry(frame3, borderwidth=5)
given_year_field = Entry(frame3, borderwidth=5)

outcome_year = Entry(frame3, borderwidth=5)
outcome_month = Entry(frame3, borderwidth=5)
outcome_day = Entry(frame3, borderwidth=5)

day_field.grid(row=1, column=1)
month_field.grid(row=2, column=1)
year_field.grid(row=3, column=1)

given_day_field.grid(row=1, column=4)
given_month_field.grid(row=2, column=4)
given_year_field.grid(row=3, column=4)

outcome_year.grid(row=6, column=1)
outcome_month.grid(row=8, column=1)
outcome_day.grid(row=10, column=1)

"""Code to add buttons to the Calculator"""
button_1 = Button(frame1, text = "1" , padx = 40, pady = 20,borderwidth=4,bg = "gray", fg = "white", command =lambda: button_click(1))
button_2 = Button(frame1, text = "2" , padx = 40, pady = 20,borderwidth=4,bg = "gray", fg = "white", command =lambda: button_click(2))
button_3 = Button(frame1, text = "3" , padx = 40, pady = 20,borderwidth=4,bg = "gray", fg = "white", command =lambda: button_click(3))
button_4 = Button(frame1, text = "4" , padx = 40, pady = 20,borderwidth=4,bg = "gray", fg = "white", command =lambda: button_click(4))
button_5 = Button(frame1, text = "5" , padx = 40, pady = 20,borderwidth=4,bg = "gray", fg = "white", command =lambda: button_click(5))
button_6 = Button(frame1, text = "6" , padx = 40, pady = 20,borderwidth=4,bg = "gray", fg = "white", command =lambda: button_click(6))
button_7 = Button(frame1, text = "7" , padx = 40, pady = 20,borderwidth=4,bg = "gray", fg = "white", command =lambda: button_click(7))
button_8 = Button(frame1, text = "8" , padx = 40, pady = 20,borderwidth=4,bg = "gray", fg = "white", command =lambda: button_click(8))
button_9 = Button(frame1, text = "9" , padx = 40, pady = 20,borderwidth=4,bg = "gray", fg = "white", command =lambda: button_click(9))
button_0 = Button(frame1, text = "0" , padx = 40, pady = 20,borderwidth=4,bg = "gray", fg = "white", command =lambda: button_click(0))

button_one = Button(frame2, text = "1" , padx = 40, pady = 20,borderwidth=4,bg = "gray", fg = "white", command =lambda: button_click(1))
button_two = Button(frame2, text = "2" , padx = 40, pady = 20,borderwidth=4,bg = "gray", fg = "white", command =lambda: button_click(2))
button_three = Button(frame2, text = "3" , padx = 40, pady = 20,borderwidth=4,bg = "gray", fg = "white", command =lambda: button_click(3))
button_four = Button(frame2, text = "4" , padx = 40, pady = 20,borderwidth=4,bg = "gray", fg = "white", command =lambda: button_click(4))
button_five = Button(frame2, text = "5" , padx = 40, pady = 20,borderwidth=4,bg = "gray", fg = "white", command =lambda: button_click(5))
button_six = Button(frame2, text = "6" , padx = 40, pady = 20,borderwidth=4,bg = "gray", fg = "white", command =lambda: button_click(6))
button_seven = Button(frame2, text = "7" , padx = 40, pady = 20,borderwidth=4,bg = "gray", fg = "white", command =lambda: button_click(7))
button_eight = Button(frame2, text = "8" , padx = 40, pady = 20,borderwidth=4,bg = "gray", fg = "white", command =lambda: button_click(8))
button_nine = Button(frame2, text = "9" , padx = 40, pady = 20,borderwidth=4,bg = "gray", fg = "white", command =lambda: button_click(9))
button_zero = Button(frame2, text = "0" , padx = 40, pady = 20,borderwidth=4,bg = "gray", fg = "white", command =lambda: button_click(0))

"""Adding operations"""
button_equal = Button(frame1, text = "=" , padx = 80, pady = 20,borderwidth=4,bg = "black", fg = "white", command = button_equal)
button_egyenlo = Button(frame2, text = "=" , padx = 40, pady = 20,borderwidth=4,bg = "orange", fg = "white", command = button_equal1)
button_clear = Button(frame1, text = "C" , padx = 80, pady = 20,borderwidth=4,bg = "black", fg = "white", command = button_clear)
button_clear1 = Button(frame2, text = "C" , padx = 40, pady = 20,borderwidth=4,bg = "orange", fg = "white", command = button_clear1)
button_osszeadas = Button(frame2, text = "+", padx = 40, pady = 20,borderwidth=4,bg = "orange", fg = "white", command = button_add)
button_add = Button(frame1, text = "+" , padx = 40, pady = 20,borderwidth=4,bg = "orange", fg = "white", command = button_add)
button_kivonas = Button(frame2, text = "-" , padx = 40, pady = 20,borderwidth=4,bg = "orange", fg = "white", command = button_subtract)
button_subtract = Button(frame1, text = "-" , padx = 40, pady = 20,borderwidth=4,bg = "orange", fg = "white", command = button_subtract)
button_szorzas = Button(frame2, text = "*" , padx = 40, pady = 20,borderwidth=4,bg = "orange", fg = "white", command = button_multiply)
button_multiply = Button(frame1, text = "*" , padx = 40, pady = 20,borderwidth=4,bg = "orange", fg = "white", command = button_multiply)
button_divide = Button(frame1, text = "/" , padx = 40, pady = 20,borderwidth=4,bg = "orange", fg = "white", command = button_divide)
button_osztas = Button(frame2, text = "/" , padx = 40, pady = 20,borderwidth=4,bg = "orange", fg = "white", command = button_divide1)
button_negyzet = Button(frame2, text = "x^2", padx = 30, pady = 20,borderwidth=4,bg = "black", fg = "white", command = button_negyzet)
button_negyzet1 = Button(frame1, text = "x^2", padx = 30, pady = 20,borderwidth=4,bg = "black", fg = "white", command = button_negyzet1)
button_abszolutertek=Button(frame2, text= "|x|", padx=30,pady=20,borderwidth=4, bg = "black", fg = "white",command = button_abszolutertek)
button_minusz=Button(frame1,text= "-/+", padx=30,pady=20,borderwidth=4,bg = "orange", fg = "white",command=button_minusz)
button_minusz1=Button(frame2,text= "-/+", padx=30,pady=20,borderwidth=4,bg = "orange", fg = "white",command=button_minusz1)
button_recip=Button(frame2, text = "1/x", padx = 30,pady = 20,borderwidth=4,bg = "black", fg = "white", command= button_recip)
button_lg= Button(frame2, text = "lg", padx = 35, pady = 20,borderwidth=4,bg = "black", fg = "white", command = button_lg)
button_sinus= Button(frame2, text = "sin", padx = 30, pady = 20,borderwidth=4,bg = "black", fg = "white", command = button_sinus)
button_cos=Button(frame2, text = "cos", padx = 30, pady = 20,borderwidth=4,bg = "black", fg = "white", command = button_cos)
button_tan=Button(frame2, text = "tan", padx = 30, pady = 20,borderwidth=4,bg = "black", fg = "white", command = button_tan)
button_ctg=Button(frame2, text = "ctg", padx = 30, pady = 20,borderwidth=4,bg = "black", fg = "white", command = button_ctg)
button_fact=Button(frame2,text = "n!", padx = 35, pady= 20,borderwidth=4,bg = "black", fg = "white", command = button_fact)
button_pi = Button(frame1, text = "pi", padx = 35, pady = 20,borderwidth=4,bg = "black", fg = "white", command = button_pipi)
button_2pi = Button(frame1, text = "2pi", padx = 30, pady = 20,borderwidth=4,bg = "black", fg = "white", command = button_2pipi)
button_pi_tudomanyos= Button(frame2, text = "pi", padx = 35,borderwidth=4, pady = 20,bg = "black", fg = "white",command = button_pipi)
button_gyok= Button (frame2, text = "sqrt", padx = 25,borderwidth=4, pady = 20,bg = "orange", fg = "white", command = button_gyok)
button_maradekos = Button(frame1, text = "%",padx = 40,borderwidth=4, pady = 20,bg = "black", fg = "white", command= button_maradek)
button_backspace = Button(frame1, text = "<<", padx = 35,borderwidth=4, pady = 20,bg = "black", fg = "white", command =lambda: button_undo())
button_bckspc = Button(frame2, text = "<<", padx = 35, pady = 20,borderwidth=4,bg = "black", fg = "white", command=lambda:button_undo())
button_pont = Button(frame2, text = ".", padx = 40, pady =20,borderwidth=4,bg = "orange", fg = "white", command =lambda: button_click(10))
button_vesszo = Button(frame1, text = ".", padx = 40, pady =20,borderwidth=4,bg = "orange", fg = "white", command =lambda: button_click(10))

"""Create fonts, For uniform button size"""
myFont=font.Font(family= 'Courier', size = 13, weight='bold')
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
button_clear1['font'] = myFont
button_add['font']=myFont
button_equal['font']=myFont
button_egyenlo['font'] = myFont
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
button_pi_tudomanyos['font']= myFont
button_gyok['font']= myFont
button_backspace['font'] = myFont
button_maradekos['font'] = myFont
button_negyzet1['font'] = myFont
button_bckspc['font'] = myFont
button_pont['font'] = myFont
button_egyenlo['font'] = myFont
button_minusz1['font'] = myFont
button_osztas['font'] = myFont
button_2pi['font'] = myFont

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

button_backspace.grid (row = 5, column = 4)
button_one.grid(row = 3, column = 0)
button_two.grid(row = 3, column = 1)
button_three.grid(row = 3, column = 2)
button_four.grid(row = 2, column = 0)
button_five.grid(row = 2, column = 1)
button_six.grid(row = 2, column = 2)
button_seven.grid(row = 1, column = 0)
button_eight.grid(row = 1, column = 1)
button_nine.grid(row = 1, column = 2)
button_zero.grid(row = 4, column = 1)

button_osszeadas.grid(row = 4, column = 4)
button_kivonas.grid(row=3, column = 4)
button_szorzas.grid(row=2,column = 4)
button_osztas.grid ( row =1, column =4 )
button_lg.grid(row=2,column = 5)
button_sinus.grid(row= 5,column = 4)
button_cos.grid(row = 5, column = 5)
button_tan.grid(row = 6, column = 4)
button_ctg.grid(row = 6, column = 5)
button_fact.grid(row = 6, column = 1)
button_pi.grid(row = 3, column = 4)
button_2pi.grid(row =1 , column = 4)
button_gyok.grid(row= 5, column = 2)
button_negyzet.grid (row = 6, column = 2)
button_negyzet1.grid (row = 4, column = 4)
button_abszolutertek.grid(row=4,column=5)
button_clear1.grid(row =4 , column=0)
button_recip.grid(row=6, column = 0)
button_pi_tudomanyos.grid(row = 3, column= 5)
button_bckspc.grid (row = 1, column = 5)
button_pont.grid(row = 4, column = 2)
button_egyenlo.grid(row = 5, column = 0)
button_minusz1.grid(row=5, column=1)

window.mainloop()