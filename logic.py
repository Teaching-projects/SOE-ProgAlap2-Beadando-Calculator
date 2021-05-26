from tkinter import *
import math
from tkinter import messagebox


class Logic():
    def __init__(self,number, f_num, second_number,current):
        self.current = current
        self.f_num = f_num
        self.second_number = second_number
        self.number = number

    def button_click(self,number):
        """Számgombok lenyomása"""
        if (number == 10):
            current = self.e.get()
            self.e.delete(0, END)
            self.e.insert(0, str(current) + ".")

        else:
            current = self.e.get()
            self.e.delete(0, END)
            self.e.insert(0, str(current) + str(number))
        # e.delete(0,END)

    def button_clear(self):
        """Entry törtlése"""
        self.e.delete(0, END)

    def button_clear1(self):
        """Entry törtlése"""
        self.e.delete(0, END)

    def button_add(self):
        """Összeadás"""
        self.first_number = self.e.get()
        self.f_num = float(self.first_number)
        self.e.delete(0,END)
        self.muv = 1

    def button_add1(self):
        """Összeadás"""
        self.first_number = self.e.get()
        self.f_num = float(self.first_number)
        self.e.delete(0,END)
        self.muv = 1

    def button_equal(self):
        """Egyenlő"""
        self.second_number = self.e.get()
        self.e.delete(0, END)
        if self.muv == 1:
            self.e.insert(0, self.f_num + float(self.second_number))
        elif self.muv == 2:
            self.e.insert(0, self.f_num - float(self.second_number))
        elif self.muv == 3:
            self.e.insert(0, self.f_num * float(self.second_number))
        elif self.muv == 4:
            self.e.insert(0, self.f_num / float(self.second_number))
        elif self.muv == 5:
            self.e.insert(0, self.f_num * float(self.f_num))
        elif self.muv == 6:
            self.e.insert(0, abs(float(self.f_num)))
        elif self.muv == 7:
            self.e.insert(0, -1 * (float(self.f_num)))
        elif self.muv == 8:
            self.e.insert(0, self.f_num % float(self.second_number))

    def button_subtract(self):
        """Kivonás"""
        self.first_number = self.e.get()
        self.f_num = float(self.first_number)
        self.e.delete(0, END)
        self.muv = 2

    def button_subtract1(self):
        """Kivonás"""
        self.first_number = self.e.get()
        self.f_num = float(self.first_number)
        self.e.delete(0, END)
        self.muv = 2

    def button_multiply(self):
        """Szorzás"""
        self.first_number = self.e.get()
        self.f_num = float(self.first_number)
        self.e.delete(0, END)
        self.muv = 3

    def button_multiply1(self):
        """Szorzás"""
        self.first_number = self.e.get()
        self.f_num = float(self.first_number)
        self.e.delete(0, END)
        self.muv = 3

    def button_divide(self):
        """Osztás"""
        self.first_number = self.e.get()
        self.f_num = float(self.first_number)
        self.e.delete(0, END)
        self.muv = 4

    def button_negyzet1(self):
        """Négyzetre emeli a számot"""
        self.first_number = self.e.get()
        self.f_num = float(self.first_number)
        self.e.delete(0, END)
        self.muv = 5

    def button_minusz(self):
        """Negatív előjelet kap a szám"""
        self.current = self.e.get()
        self.e.delete(0, END)
        self.e.insert(0, -1 * float(self.current))

    def button_undo(self):
        """Visszavonás"""
        length = len(self.e.get())
        self.e.delete(length - 1, 'end')
        if length == 1:
            self.e.insert(0, "0")

    def button_pipi(self):
        """Pi értéke"""
        if self.e.get() == "0":
            self.e.delete(0, END)
        length = len(self.e.get())
        self.e.insert(length, str(math.pi))

    def button_2pipi(self):
        """2*pi"""
        if self.e.get() == "0":
            self.e.delete(0, END)
        length = len(self.e.get())
        self.e.insert(length, str(math.tau))

    def button_maradek(self):
        """Maradékos osztás"""
        self.first_number = self.e.get()
        self.f_num = float(self.first_number)
        self.e.delete(0, END)
        self.muv = 8

    """Scientific calculator metods"""

    def button_equal1(self):
        """Egyenlőség"""
        self.second_number = self.e.get()
        self.e.delete(0, END)
        if self.muv == 1:
            self.e.insert(0, self.f_num + float(self.second_number))
        elif self.muv == 2:
            self.e.insert(0, self.f_num - float(self.second_number))
        elif self.muv == 3:
            self.e.insert(0, self.f_num * float(self.second_number))
        elif self.muv == 4:
            self.e.insert(0, self.f_num / float(self.second_number))
        elif self.muv == 5:
            self.e.insert(0, self.f_num * float(self.f_num))
        elif self.muv == 6:
            self.e.insert(0, abs(float(self.f_num)))
        elif self.muv == 7:
            self.e.insert(0, -1 * (float(self.f_num)))
        elif self.muv == 8:
            self.e.insert(0, self.f_num % float(self.second_number))

    def button_divide1(self):
        """Osztás"""
        self.first_number = self.e.get()
        self.f_num = float(self.first_number)
        self.e.delete(0, END)
        self.muv = 4

    def button_negyzet(self):
        """Négyzetre emelés"""
        self.first_number = self.e.get()
        self.f_num = float(self.first_number)
        self.e.delete(0, END)
        self.muv = 5

    def button_abszolutertek(self):
        """Számnak az abszolútértéke"""
        self.current = self.e.get()
        self.e.delete(0, END)
        self.e.insert(0, abs(float(self.current)))

    def button_minusz1(self):
        """Negatív előjel"""
        self.current = self.e.get()
        self.e.delete(0, END)
        self.e.insert(0, -1 * float(self.current))

    def button_recip(self):
        """Számanak a reciproka"""
        self.current = self.e.get()
        self.e.delete(0, END)
        self.e.insert(0, 1 / float(self.current))

    def button_lg(self):
        """Számnak a tizes alapú logaritmusa"""
        self.current = self.e.get()
        self.e.delete(0, END)
        self.e.insert(0, math.log(float(self.current), 10))

    def button_sinus(self):
        """Számnak a sinusa"""
        self.current = self.e.get()
        self.e.delete(0, END)
        self.e.insert(0, math.sin(float(self.current)))

    def button_cos(self):
        """Számnak a cosinusa"""
        self.current = self.e.get()
        self.e.delete(0, END)
        self.e.insert(0, math.cos(float(self.current)))

    def button_ctg(self):
        """Számnak a cotangense"""
        self.current = self.e.get()
        self.e.delete(0, END)
        self.e.insert(0, 1 / math.tan(float(self.current)))

    def button_tan(self):
        """Számnak a tangense"""
        self.current = self.e.get()
        self.e.delete(0, END)
        self.e.insert(0, math.tan(float(self.current)))

    def button_fact(self):
        """Számnak a factoriálja"""
        self.current = self.e.get()
        self.e.delete(0, END)
        self.e.insert(0, math.factorial(float(self.current)))

    def button_gyok(self):
        """Számnak a gyöke"""
        self.current = self.e.get()
        self.e.delete(0, END)
        self.e.insert(0, math.sqrt(float(self.current)))

    def converter(self):
        """Átváltások"""
        self.km = float(self.ent1.get()) / 1000
        self.mm = float(self.ent1.get()) * 1000
        self.cm = float(self.ent1.get()) * 100
        self.mf = float(self.ent1.get()) * 0.00062
        self.yard = float(self.ent1.get()) * 1.094
        self.inch = float(self.ent1.get()) * 39.37
        self.lab = float(self.ent1.get()) * 3.281

        self.text1.delete("1.0", END)
        self.text1.insert(END, self.km)

        self.text2.delete("1.0", END)
        self.text2.insert(END, self.mm)

        self.text3.delete("1.0", END)
        self.text3.insert(END, self.cm)

        self.text4.delete("1.0", END)
        self.text4.insert(END, self.mf)

        self.text5.delete("1.0", END)
        self.text5.insert(END, self.yard)

        self.text6.delete("1.0", END)
        self.text6.insert(END, self.inch)

        self.text7.delete("1.0", END)
        self.text7.insert(END, self.lab)

    def clearAll(self):
        """Mezők törlése"""
        self.day_field.delete(0, END)
        self.month_field.delete(0, END)
        self.year_field.delete(0, END)
        self.given_day_field.delete(0, END)
        self.given_month_field.delete(0, END)
        self.given_year_field.delete(0, END)
        self.outcome_day.delete(0, END)
        self.outcome_month.delete(0, END)
        self.outcome_year.delete(0, END)

    def Error(self):
        """Ha egy mező üresen marad"""
        if (self.day_field.get() == "" or self.month_field.get() == ""
                or self.year_field.get() == "" or self.given_day_field.get() == ""
                or self.given_month_field.get() == "" or self.given_year_field.get() == ""):
            messagebox.showerror("Error", "Some field is empty")
            self.clearAll()
            return -1

    def calculateDate(self):
        """Dátum kalkulátor"""
        self.value = self.Error()
        if self.value == -1:
            return

        else:
            self.dk_day = int(self.day_field.get())
            self.dk_month = int(self.month_field.get())
            self.dk_year = int(self.year_field.get())

            self.given_day = int(self.given_day_field.get())
            self.given_month = int(self.given_month_field.get())
            self.given_year = int(self.given_year_field.get())

            self.month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

            if (self.dk_day > self.given_day):
                self.given_month = self.given_month - 1
                self.given_day = self.given_day + self.month[self.dk_month - 1]

            if (self.dk_month > self.given_month):
                self.given_year = self.given_year - 1
                self.given_month = self.given_month + 12

            self.calculated_day = self.given_day - self.dk_day
            self.calculated_month = self.given_month - self.dk_month
            self.calculated_year = self.given_year - self.dk_year

            self.outcome_day.insert(10, str(self.calculated_day))
            self.outcome_month.insert(10, str(self.calculated_month))
            self.outcome_year.insert(10, str(self.calculated_year))