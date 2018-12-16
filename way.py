import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import run_file
import pandas as pd
from tkinter import messagebox

class Fil(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):

        self.v1 = tk.BooleanVar()
        self.v2 = tk.BooleanVar()
        self.v3 = tk.BooleanVar()
        self.v4 = tk.BooleanVar()
        self.v4 = tk.BooleanVar()
        self.v5 = tk.BooleanVar()

        self.init_canvas()

        self.init_filter_time()
        self.init_filter_datetime()
        self.init_filter_square()
        self.init_filter_area()


        self.refresh = tk.Checkbutton(self, variable= self.v5)
        self.refresh["text"] = "refresh the data?"
        self.refresh.pack(side="top")


        self.quit = tk.Button(self, text="GO", fg="red",
                              command=self.on_click)
        self.quit.pack(side="top")

    def init_canvas(self):
        self.f = plt.figure(figsize=(5, 5))
        self.canvas = FigureCanvasTkAgg(self.f, self)
        self.canvas.get_tk_widget().pack(side="left")

        self.var = tk.StringVar()
        self.descrebtion = tk.Label(self, textvariable=self.var, height=2, width=35)
        self.var.set("")
        self.descrebtion.pack(side="left")

    def init_filter_area(self):
        self.filterarea = tk.Checkbutton(self, variable=self.v4, command = self.clear_area)
        self.filterarea["text"] = "filter By area"
        self.filterarea.pack(side="top")

        self.var6 = tk.StringVar()
        self.descrebtion6 = tk.Label(self, textvariable=self.var6, height=2, width=80)
        self.var6.set("enter top x, top y, top x, top y")
        self.descrebtion3.pack(side="top")

        self.x1 = tk.Text(self, height=1, width=15)
        self.x1.pack(side="top")
        self.y1 = tk.Text(self, height=1, width=15)
        self.y1.pack(side="top")
        self.x2 = tk.Text(self, height=1, width=15)
        self.x2.pack(side="top")
        self.y2 = tk.Text(self, height=1, width=15)
        self.y2.pack(side="top")

    def init_filter_square(self):

        self.filtersquare = tk.Checkbutton(self, variable= self.v3,command = self.clear_square)
        self.filtersquare["text"] = "filter By square"
        self.filtersquare.pack(side="top")

        self.var5 = tk.StringVar()
        self.descrebtion5 = tk.Label(self, textvariable=self.var5, height=2, width=80)
        self.var5.set("enter the wanted squares lost")
        self.descrebtion5.pack(side="top")

        self.square = tk.Text(self, height = 1, width = 30)
        self.square.pack(side="top")

    def init_filter_datetime(self):

        self.filterdatetime = tk.Checkbutton(self, variable= self.v2, command = self.clear_datetime)
        self.filterdatetime["text"] = "filter By date time"
        self.filterdatetime.pack(side="top")

        self.var3 = tk.StringVar()
        self.descrebtion3 = tk.Label(self, textvariable=self.var3, height=2, width=80)
        self.var3.set("enter the first date time yyyy-mm-dd hh:mm:ss")
        self.descrebtion3.pack(side="top")


        self.datetimebe = tk.Text(self, height = 1, width = 30)
        self.datetimebe.pack(side="top")

        self.var4 = tk.StringVar()
        self.descrebtion4 = tk.Label(self, textvariable=self.var4, height=2, width=80)
        self.var4.set("enter the first date time yyyy-mm-dd hh:mm:ss")
        self.descrebtion4.pack(side="top")


        self.datetimeaf = tk.Text(self, height = 1, width = 30)
        self.datetimeaf.pack(side="top")

    def init_filter_time(self):
        self.filtertime = tk.Checkbutton(self, variable= self.v1, command = self.clear_time)
        self.filtertime["text"] = "filter By time"
        self.filtertime.pack(side="top")

        self.var1 = tk.StringVar()
        self.descrebtion1 = tk.Label(self, textvariable=self.var1, height=2, width=80)
        self.var1.set("enter the first time hh:mm:ss")
        self.descrebtion1.pack(side="top")

        self.timebe = tk.Text(self, height = 1, width = 30)
        self.timebe.pack(side = "top")

        self.var2 = tk.StringVar()
        self.descrebtion2 = tk.Label(self, textvariable=self.var2, height=2, width=80)
        self.var2.set("enter the last time hh:mm:ss")
        self.descrebtion2.pack(side="top")

        self.timeaf = tk.Text(self, height = 1, width = 30)
        self.timeaf.pack(side="top")

    def clear_time(self):
        v1 = self.v1.get()
        if not v1:
            self.timeaf.delete('1.0', 'end-1c')
            self.timebe.delete('1.0', 'end-1c')

    def clear_datetime(self):
        v1 = self.v2.get()
        if not v1:
            self.datetimeaf.delete('1.0', 'end-1c')
            self.datetimebe.delete('1.0', 'end-1c')

    def clear_square(self):
        v1 = self.v3.get()
        if not v1:
            self.square.delete('1.0', 'end-1c')


    def clear_area(self):
        v1 = self.v4.get()
        if not v1:
            self.y2.delete('1.0', 'end-1c')
            self.y1.delete('1.0', 'end-1c')
            self.x2.delete('1.0', 'end-1c')
            self.x1.delete('1.0', 'end-1c')

    def on_click(self):

        plt.gcf().clear()
        desc = ""
        v1 =self.v1.get()
        v2 =self.v2.get()
        v3 =self.v3.get()
        v4 =self.v4.get()

        print(self.v1)
        print(self.v2)
        if v1 and v3:
            t1 = self.timebe.get("1.0", "end-1c")
            t2 = self.timeaf.get("1.0", "end-1c")

            try:
                pd.to_datetime(t1).time()
            except:
                messagebox.showinfo("Invalid Input", "invalid time!")
                return
            # t2 = input('enter last range of time in format hh:mm:ss\n')
            try:
                pd.to_datetime(t2).time()
            except:
                messagebox.showinfo("Invalid Input", "invalid time!")
                return

            v = self.v5.get()
            text = self.square.get("1.0", "end-1c")

            if not run_file.v.cone.cheak_list(text):
                messagebox.showinfo("Invalid Input", "invalid list!")
                return

            run_file.v.cone.rap_filter_by_time_chossen_squere(t1, t2, text, v)
            desc += f"filter by time and squares:\n the range is: ({t1} , {t2})\nthe squares are [{text}]\n "


        elif v2 and v3:
            t1 = self.datetimebe.get("1.0", "end-1c")
            t2 = self.datetimeaf.get("1.0", "end-1c")

            try:
                pd.to_datetime(t1)
            except:
                messagebox.showinfo("Invalid Input", "invalid date time!")
                return

            # t2 = input('enter last range of time in format hh:mm:ss\n')
            try:
                pd.to_datetime(t2)
            except:
                messagebox.showinfo("Invalid Input", "invalid date time!")
                return

            v = self.v5.get()
            text = self.square.get("1.0", "end-1c")

            if not run_file.v.cone.cheak_list(text):
                messagebox.showinfo("Invalid Input", "invalid list!")
                return

            run_file.v.cone.rap_filter_by_date_time_chossen_squere(t1, t2, text, v)

            desc += f"filter by time and squares:\n the range is: ({t1} , {t2})\nthe squares are [{text}]\n "

        elif v1:
            t1 = self.timebe.get("1.0", "end-1c")
            t2 = self.timeaf.get("1.0", "end-1c")
            print(t1)
            print(t2)
            try:
                pd.to_datetime(t1).time()
            except:
                messagebox.showinfo("Invalid Input", "invalid time!")
                return

            # t2 = input('enter last range of time in format hh:mm:ss\n')
            try:
                pd.to_datetime(t2).time()
            except:
                messagebox.showinfo("Invalid Input", "invalid time!")
                return

            v =self.v5.get()

            run_file.v.cone.rap_filter_by_time(t1, t2, v)
            print(self.timebe)
            print(self.timeaf)
            print(self.refresh)

            desc += f"filter by time:\n the range is ({t1} , {t2})\n"
        elif v2:

            t1 = self.datetimebe.get("1.0", "end-1c")
            t2 = self.datetimeaf.get("1.0", "end-1c")

            print(t1)
            print(t2)
            try:
                pd.to_datetime(t1)
            except:
                messagebox.showinfo("Invalid Input", "invalid date time!")
                return

            # t2 = input('enter last range of time in format hh:mm:ss\n')
            try:
                pd.to_datetime(t2)
            except:
                messagebox.showinfo("Invalid Input", "invalid date time!")
                return

            v = self.v5.get()
            run_file.v.cone.rap_filter_by_date_time(t1, t2, v)

            desc += f"filter by time:\n the range is ({t1} , {t2})\n"
        elif v3:
            text = self.square.get("1.0", "end-1c")

            if not run_file.v.cone.cheak_list(text):
                messagebox.showinfo("Invalid Input", "invalid list!")
                return

            v = self.v5.get()
            run_file.v.cone.rap_filter_by_chossen_squere(text, v)
            desc += f"filter by square:\n the squares are [{text}]\n"
        elif v4:
            x1 = self.x1.get("1.0", "end-1c")
            y1 = self.y1.get("1.0", "end-1c")
            x2 = self.x2.get("1.0", "end-1c")
            y2 = self.y2.get("1.0", "end-1c")

            v = self.v5.get()

            run_file.v.cone.rap_filter_by_area(x1, y1, x2, y2, v)
            desc += f"filter by area:\n the range is ({x1},{y1},{x2},{y2})\n"

        self.var.set(desc)


        # f = Figure(figsize=(5, 5), dpi=100)
        # ab = f.add_subplot(111)

        pa = run_file.v.cone.m.filter_req.groupby(['obj', 'filename']).size()
        print("!!!!!!!!!!!!!!")
        for t in pa.index:
            oo = run_file.v.cone.m.df_by_obj.loc[t]
            plt.plot(oo.x, oo.y)
        plt.imshow(run_file.v.cone.m.image)

        print("**********************************")
        self.canvas.draw()
            # self.line, = ab.plot(range(24))
            # self.canvas = FigureCanvasTkAgg(f, self)
            # self.canvas.get_tk_widget().pack(side = "bottom")
            # print(self.canvas.get_tk_widget().place)

