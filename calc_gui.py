from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.font as font
import logic as logic

class GUI(logic.Logic):
    def __init__(self):
        super(logic.Logic, self).__init__()
        self.window = tk.Tk()
        self.window.title("Számológép")
        self.window.geometry("535x541")

        """Notebook létrehozása"""
        self.notebook = ttk.Notebook(self.window)
        self.notebook.pack(pady=50, expand=True)
        self.notebook.grid(row=1, column=0)

        """Framek létrehozása"""
        self.frame0 = ttk.Frame(self.window)
        self.frame0.grid(row=0, column=0)
        self.frame1 = ttk.Frame(self.notebook, width=535, height=462)
        self.frame2 = ttk.Frame(self.notebook, width=535, height=462)
        self.frame3 = ttk.Frame(self.notebook, width=535, height=462)
        self.frame4 = ttk.Frame(self.notebook, width=535, height=462)

        # self.frame0.pack(fill='both', expand=True)
        self.frame1.pack(fill='both', expand=True)
        self.frame2.pack(fill='both', expand=True)
        self.frame3.pack(fill='both', expand=True)
        self.frame4.pack(fill='both', expand=True)

        self.notebook.add(self.frame1, text='Általános')
        self.notebook.add(self.frame2, text='Tudományos')
        self.notebook.add(self.frame3, text='Dátumszámítás')
        self.notebook.add(self.frame4, text='Hossz átváltás')

        """Entry létrehozása"""
        self.e = Entry(self.frame0, width=50, borderwidth=10)
        self.e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        self.e.insert(0, "  ")

        """Általános gombok"""
        self.button_1 = Button(self.frame1, text="1", padx=40, pady=20, borderwidth=4, bg="gray", fg="white",
                                command=lambda:self.button_click(1))
        self.button_2 = Button(self.frame1, text="2", padx=40, pady=20, borderwidth=4, bg="gray", fg="white",
                               command=lambda: self.button_click(2))
        self.button_3 = Button(self.frame1, text="3", padx=40, pady=20, borderwidth=4, bg="gray", fg="white",
                               command=lambda: self.button_click(3))
        self.button_4 = Button(self.frame1, text="4", padx=40, pady=20, borderwidth=4, bg="gray", fg="white",
                               command=lambda:self.button_click(4))
        self.button_5 = Button(self.frame1, text="5", padx=40, pady=20, borderwidth=4, bg="gray", fg="white",
                               command=lambda:self.button_click(5))
        self.button_6 = Button(self.frame1, text="6", padx=40, pady=20, borderwidth=4, bg="gray", fg="white",
                               command=lambda:self.button_click(6))
        self.button_7 = Button(self.frame1, text="7", padx=40, pady=20, borderwidth=4, bg="gray", fg="white",
                               command=lambda: self.button_click(7))
        self.button_8 = Button(self.frame1, text="8", padx=40, pady=20, borderwidth=4, bg="gray", fg="white",
                               command=lambda:self.button_click(8))
        self.button_9 = Button(self.frame1, text="9", padx=40, pady=20, borderwidth=4, bg="gray", fg="white",
                               command=lambda:self.button_click(9))
        self.button_0 = Button(self.frame1, text="0", padx=40, pady=20, borderwidth=4, bg="gray", fg="white",
                               command=lambda:self.button_click(0))

        """Általános gombok elhelyezkedése"""
        self.button_1.grid(row=3, column=0)
        self.button_2.grid(row=3, column=1)
        self.button_3.grid(row=3, column=2)
        self.button_4.grid(row=2, column=0)
        self.button_5.grid(row=2, column=1)
        self.button_6.grid(row=2, column=2)
        self.button_7.grid(row=1, column=0)
        self.button_8.grid(row=1, column=1)
        self.button_9.grid(row=1, column=2)
        self.button_0.grid(row=4, column=1)

        """Általános funkciók"""
        self.button_equal = Button(self.frame1, text="=", padx=80, pady=20, borderwidth=4, bg="black", fg="white",
                                   command=self.button_equal)
        self.button_clear = Button(self.frame1, text="C", padx=80, pady=20, borderwidth=4, bg="black", fg="white",
                                   command=self.button_clear)
        self.button_add = Button(self.frame1, text="+", padx=40, pady=20, borderwidth=4, bg="orange", fg="white",
                                 command=self.button_add)
        self.button_subtract = Button(self.frame1, text="-", padx=40, pady=20, borderwidth=4, bg="orange", fg="white",
                                      command=self.button_subtract)
        self.button_multiply = Button(self.frame1, text="*", padx=40, pady=20, borderwidth=4, bg="orange", fg="white",
                                      command=self.button_multiply)
        self.button_divide = Button(self.frame1, text="/", padx=40, pady=20, borderwidth=4, bg="orange", fg="white",
                                    command=self.button_divide)
        self.button_negyzet1 = Button(self.frame1, text="x^2", padx=30, pady=20, borderwidth=4, bg="black", fg="white",
                                      command=self.button_negyzet1)
        self.button_minusz = Button(self.frame1, text="-/+", padx=30, pady=20, borderwidth=4, bg="orange", fg="white",
                                    command=self.button_minusz)
        self.button_pi = Button(self.frame1, text="pi", padx=35, pady=20, borderwidth=4, bg="black", fg="white",
                                command=self.button_pipi)
        self.button_2pi = Button(self.frame1, text="2pi", padx=30, pady=20, borderwidth=4, bg="black", fg="white",
                                 command=self.button_2pipi)
        self.button_maradekos = Button(self.frame1, text="%", padx=40, borderwidth=4, pady=20, bg="black", fg="white",
                                       command=self.button_maradek)
        self.button_backspace = Button(self.frame1, text="<<", padx=35, borderwidth=4, pady=20, bg="black", fg="white",
                                       command=lambda: self.button_undo())
        self.button_vesszo = Button(self.frame1, text=".", padx=40, pady=20, borderwidth=4, bg="orange", fg="white",
                                    command=lambda: self.button_click(10))

        """Általános funkció gombok elhelyezkedése"""
        self.button_clear.grid(row=5, column=0, columnspan=2, sticky=N + S + E + W)
        self.button_add.grid(row=4, column=3)
        self.button_equal.grid(row=5, column=2, columnspan=2, sticky=N + S + E + W)
        self.button_subtract.grid(row=3, column=3)
        self.button_multiply.grid(row=2, column=3)
        self.button_divide.grid(row=1, column=3)
        self.button_vesszo.grid(row=4, column=2)
        self.button_maradekos.grid(row=2, column=4, sticky=N + S + E + W)
        self.button_minusz.grid(row=4, column=0)
        self.button_backspace.grid(row=5, column=4)
        self.button_pi.grid(row=3, column=4)
        self.button_2pi.grid(row=1, column=4)
        self.button_negyzet1.grid(row=4, column=4)

        """Tudományos gombok"""
        self.button_one = Button(self.frame2, text="1", padx=40, pady=20, borderwidth=4, bg="gray", fg="white",
                                 command=lambda: self.button_click(1))
        self.button_two = Button(self.frame2, text="2", padx=40, pady=20, borderwidth=4, bg="gray", fg="white",
                                 command=lambda: self.button_click(2))
        self.button_three = Button(self.frame2, text="3", padx=40, pady=20, borderwidth=4, bg="gray", fg="white",
                                   command=lambda: self.button_click(3))
        self.button_four = Button(self.frame2, text="4", padx=40, pady=20, borderwidth=4, bg="gray", fg="white",
                                  command=lambda: self.button_click(4))
        self.button_five = Button(self.frame2, text="5", padx=40, pady=20, borderwidth=4, bg="gray", fg="white",
                                  command=lambda: self.button_click(5))
        self.button_six = Button(self.frame2, text="6", padx=40, pady=20, borderwidth=4, bg="gray", fg="white",
                                 command=lambda: self.button_click(6))
        self.button_seven = Button(self.frame2, text="7", padx=40, pady=20, borderwidth=4, bg="gray", fg="white",
                                   command=lambda: self.button_click(7))
        self.button_eight = Button(self.frame2, text="8", padx=40, pady=20, borderwidth=4, bg="gray", fg="white",
                                   command=lambda: self.button_click(8))
        self.button_nine = Button(self.frame2, text="9", padx=40, pady=20, borderwidth=4, bg="gray", fg="white",
                                  command=lambda: self.button_click(9))
        self.button_zero = Button(self.frame2, text="0", padx=40, pady=20, borderwidth=4, bg="gray", fg="white",
                                  command=lambda: self.button_click(0))

        """Tudományos gombok elhelyezkedése"""
        self.button_one.grid(row=3, column=0)
        self.button_two.grid(row=3, column=1)
        self.button_three.grid(row=3, column=2)
        self.button_four.grid(row=2, column=0)
        self.button_five.grid(row=2, column=1)
        self.button_six.grid(row=2, column=2)
        self.button_seven.grid(row=1, column=0)
        self.button_eight.grid(row=1, column=1)
        self.button_nine.grid(row=1, column=2)
        self.button_zero.grid(row=4, column=1)

        """Tudományos funkció gombok"""
        self.button_egyenlo = Button(self.frame2, text="=", padx=40, pady=20, borderwidth=4, bg="orange", fg="white",
                                     command=self.button_equal1)
        self.button_clear1 = Button(self.frame2, text="C", padx=40, pady=20, borderwidth=4, bg="orange", fg="white",
                                    command=self.button_clear1)
        self.button_osszeadas = Button(self.frame2, text="+", padx=40, pady=20, borderwidth=4, bg="orange", fg="white",
                                       command=self.button_add1)
        self.button_kivonas = Button(self.frame2, text="-", padx=40, pady=20, borderwidth=4, bg="orange", fg="white",
                                     command=self.button_subtract1)
        self.button_szorzas = Button(self.frame2, text="*", padx=40, pady=20, borderwidth=4, bg="orange", fg="white",
                                     command=self.button_multiply1)
        self.button_osztas = Button(self.frame2, text="/", padx=40, pady=20, borderwidth=4, bg="orange", fg="white",
                                    command=self.button_divide1)
        self.button_negyzet = Button(self.frame2, text="x^2", padx=30, pady=20, borderwidth=4, bg="black", fg="white",
                                     command=self.button_negyzet)
        self.button_abszolutertek = Button(self.frame2, text="|x|", padx=30, pady=20, borderwidth=4, bg="black",
                                           fg="white", command=self.button_abszolutertek)
        self.button_minusz1 = Button(self.frame2, text="-/+", padx=30, pady=20, borderwidth=4, bg="orange", fg="white",
                                     command=self.button_minusz1)
        self.button_recip = Button(self.frame2, text="1/x", padx=30, pady=20, borderwidth=4, bg="black", fg="white",
                                   command=self.button_recip)
        self.button_lg = Button(self.frame2, text="lg", padx=35, pady=20, borderwidth=4, bg="black", fg="white",
                                command=self.button_lg)
        self.button_sinus = Button(self.frame2, text="sin", padx=30, pady=20, borderwidth=4, bg="black", fg="white",
                                   command=self.button_sinus)
        self.button_cos = Button(self.frame2, text="cos", padx=30, pady=20, borderwidth=4, bg="black", fg="white",
                                 command=self.button_cos)
        self.button_tan = Button(self.frame2, text="tan", padx=30, pady=20, borderwidth=4, bg="black", fg="white",
                                 command=self.button_tan)
        self.button_ctg = Button(self.frame2, text="ctg", padx=30, pady=20, borderwidth=4, bg="black", fg="white",
                                 command=self.button_ctg)
        self.button_fact = Button(self.frame2, text="n!", padx=35, pady=20, borderwidth=4, bg="black", fg="white",
                                  command=self.button_fact)
        self.button_pi_tudomanyos = Button(self.frame2, text="pi", padx=35, borderwidth=4, pady=20, bg="black",
                                           fg="white",
                                           command=self.button_pipi)
        self.button_gyok = Button(self.frame2, text="sqrt", padx=25, borderwidth=4, pady=20, bg="orange", fg="white",
                                  command=self.button_gyok)
        self.button_bckspc = Button(self.frame2, text="<<", padx=35, pady=20, borderwidth=4, bg="black", fg="white",
                                    command=lambda: self.button_undo())
        self.button_pont = Button(self.frame2, text=".", padx=40, pady=20, borderwidth=4, bg="orange", fg="white",
                                  command=lambda: self.button_click(10))

        """Tudományos funkció gombok elhelyezkedése"""
        self.button_osszeadas.grid(row=4, column=4)
        self.button_kivonas.grid(row=3, column=4)
        self.button_szorzas.grid(row=2, column=4)
        self.button_osztas.grid(row=1, column=4)
        self.button_lg.grid(row=2, column=5)
        self.button_sinus.grid(row=5, column=4)
        self.button_cos.grid(row=5, column=5)
        self.button_tan.grid(row=6, column=4)
        self.button_ctg.grid(row=6, column=5)
        self.button_fact.grid(row=6, column=1)
        self.button_gyok.grid(row=5, column=2)
        self.button_negyzet.grid(row=6, column=2)
        self.button_abszolutertek.grid(row=4, column=5)
        self.button_clear1.grid(row=4, column=0)
        self.button_recip.grid(row=6, column=0)
        self.button_pi_tudomanyos.grid(row=3, column=5)
        self.button_bckspc.grid(row=1, column=5)
        self.button_pont.grid(row=4, column=2)
        self.button_egyenlo.grid(row=5, column=0)
        self.button_minusz1.grid(row=5, column=1)

        """Dátumszámításnál a Labelek"""
        self.start_date = Label(self.frame3, text="Dátum kezdete").grid(row=0, column=1)
        self.given_date = Label(self.frame3, text="Dátum vége").grid(row=0, column=4)
        self.nap = Label(self.frame3, text="Nap").grid(row=1, column=0)
        self.honap = Label(self.frame3, text="Hónap").grid(row=2, column=0)
        self.ev = Label(self.frame3, text="Év").grid(row=3, column=0)
        self.given_day = Label(self.frame3, text="Megadott nap").grid(row=1, column=3)
        self.given_month = Label(self.frame3, text="Megadott hónap").grid(row=2, column=3)
        self.given_year = Label(self.frame3, text="Megadott év").grid(row=3, column=3)
        self.outcome_year = Label(self.frame3, text="Év").grid(row=6, column=0)
        self.outcome_month = Label(self.frame3, text="Hónap").grid(row=8, column=0)
        self.outcome_day = Label(self.frame3, text="Nap").grid(row=10, column=0)
        self.outcome_age = Button(self.frame3, text="Különbség", command=self.calculateDate).grid(row=4, column=1)
        self.torles = Button(self.frame3, text="Törlés", command=self.clearAll).grid(row=12, column=1)

        """Dátumszámítás Entry és elhelyezkedés"""
        self.day_field = Entry(self.frame3, borderwidth=5)
        self.month_field = Entry(self.frame3, borderwidth=5)
        self.year_field = Entry(self.frame3, borderwidth=5)

        self.given_day_field = Entry(self.frame3, borderwidth=5)
        self.given_month_field = Entry(self.frame3, borderwidth=5)
        self.given_year_field = Entry(self.frame3, borderwidth=5)

        self.outcome_year = Entry(self.frame3, borderwidth=5)
        self.outcome_month = Entry(self.frame3, borderwidth=5)
        self.outcome_day = Entry(self.frame3, borderwidth=5)

        self.day_field.grid(row=1, column=1)
        self.month_field.grid(row=2, column=1)
        self.year_field.grid(row=3, column=1)

        self.given_day_field.grid(row=1, column=4)
        self.given_month_field.grid(row=2, column=4)
        self.given_year_field.grid(row=3, column=4)

        self.outcome_year.grid(row=6, column=1)
        self.outcome_month.grid(row=8, column=1)
        self.outcome_day.grid(row=10, column=1)

        """Hossz átváltás"""
        self.ent1 = StringVar()
        self.label1 = Label(self.frame4, text="Hossz méterben").grid(row=0, column=0)
        self.ent = Entry(self.frame4, borderwidth=5, textvariable=self.ent1).grid(row=0, column=1)
        self.label3 = Label(self.frame4, text='kilóméter').grid(row=4, column=0)
        self.label4 = Label(self.frame4, text='miliméter').grid(row=2, column=0)
        self.label5 = Label(self.frame4, text='centiméter').grid(row=3, column=0)
        self.label6 = Label(self.frame4, text='mérföld').grid(row=2, column=2)
        self.label7 = Label(self.frame4, text='yard').grid(row=4, column=2)
        self.label8 = Label(self.frame4, text='inch').grid(row=3, column=2)
        self.label9 = Label(self.frame4, text='láb').grid(row=5, column=0)

        self.text1 = Text(self.frame4, height=1, width=15, borderwidth=5)
        self.text2 = Text(self.frame4, height=1, width=15, borderwidth=5)
        self.text3 = Text(self.frame4, height=1, width=15, borderwidth=5)
        self.text4 = Text(self.frame4, height=1, width=15, borderwidth=5)
        self.text5 = Text(self.frame4, height=1, width=15, borderwidth=5)
        self.text6 = Text(self.frame4, height=1, width=15, borderwidth=5)
        self.text7 = Text(self.frame4, height=1, width=15, borderwidth=5)

        self.atvalt = Button(self.frame4, text="Átváltás", command=self.converter)
        self.atvalt.grid(row=1, column=1)

        self.text1.grid(row=4, column=1)
        self.text2.grid(row=2, column=1)
        self.text3.grid(row=3, column=1)
        self.text4.grid(row=2, column=3)
        self.text5.grid(row=4, column=3)
        self.text6.grid(row=3, column=3)
        self.text7.grid(row=5, column=1)



        """Egységes nagyságért felelős"""
        self.myFont =font.Font(family='Courier', size=13, weight='bold')
        self.button_1['font'] = self.myFont
        self.button_2['font'] = self.myFont
        self.button_3['font'] = self.myFont
        self.button_4['font'] = self.myFont
        self.button_5['font'] = self.myFont
        self.button_6['font'] = self.myFont
        self.button_7['font'] = self.myFont
        self.button_8['font'] = self.myFont
        self.button_9['font'] = self.myFont
        self.button_0['font'] = self.myFont
        self.button_one['font'] = self.myFont
        self.button_two['font'] = self.myFont
        self.button_three['font'] = self.myFont
        self.button_four['font'] = self.myFont
        self.button_five['font'] = self.myFont
        self.button_six['font'] = self.myFont
        self.button_seven['font'] = self.myFont
        self.button_eight['font'] = self.myFont
        self.button_nine['font'] = self.myFont
        self.button_zero['font'] = self.myFont
        self.button_osszeadas['font'] = self.myFont
        self.button_kivonas['font'] = self.myFont
        self.button_szorzas['font'] = self.myFont
        self.button_clear1['font'] = self.myFont
        self.button_add['font'] = self.myFont
        self.button_equal['font'] = self.myFont
        self.button_egyenlo['font'] = self.myFont
        self.button_clear['font'] = self.myFont
        self.button_subtract['font'] = self.myFont
        self.button_multiply['font'] = self.myFont
        self.button_divide['font'] = self.myFont
        self.button_vesszo['font'] = self.myFont
        self.button_negyzet['font'] = self.myFont
        self.button_abszolutertek['font'] = self.myFont
        self.button_minusz['font'] = self.myFont
        self.button_recip['font'] = self.myFont
        self.button_lg['font'] = self.myFont
        self.button_sinus['font'] = self.myFont
        self.button_cos['font'] = self.myFont
        self.button_tan['font'] = self.myFont
        self.button_ctg['font'] = self.myFont
        self.button_fact['font'] = self.myFont
        self.button_pi['font'] = self.myFont
        self.button_pi_tudomanyos['font'] = self.myFont
        self.button_gyok['font'] = self.myFont
        self.button_backspace['font'] = self.myFont
        self.button_maradekos['font'] = self.myFont
        self.button_negyzet1['font'] = self.myFont
        self.button_bckspc['font'] = self.myFont
        self.button_pont['font'] = self.myFont
        self.button_egyenlo['font'] = self.myFont
        self.button_minusz1['font'] = self.myFont
        self.button_osztas['font'] = self.myFont
        self.button_2pi['font'] = self.myFont

        self.window.mainloop()

GUI()
