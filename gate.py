import tkinter as tk
from way import Fil
root = tk.Tk()
import  run_file

class Main_gui(tk.Frame):
    def __init__(self):

        w = tk.Label(root, text=" Wellcome to our program!", fg="green", font="Verdana 20 bold")
        w.pack()

        f_name = tk.Label(root, text="Enter your file name ").pack()
        self.f_name = tk.Entry(root)
        self.f_name.insert(0, " ")
        self.f_name.pack()
        im_name = tk.Label(root, text="Enter your image name ").pack()
        self.i_name = tk.Entry(root)
        self.i_name.insert(0, " ")
        self.i_name.pack()

        button = tk.Button(root, text="NEXT", command=self.on_click)
        button.pack(side=tk.TOP)
        root.mainloop()


    def on_click(self):
        self.file_name = self.f_name.get()
        print(self.file_name)
        self.image_name = self.i_name.get()
        if self.image_name == " ":
           self.image_name = "data/paths0.png"
        print(self.image_name)
        run_file.load_v(self.file_name,self.image_name)
        root.destroy()
        g = Fil()