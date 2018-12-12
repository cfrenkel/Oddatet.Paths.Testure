import matplotlib.pyplot as plt
import pandas as pd
import paths.controller as c

class View:

    def __init__(self):
        self.cone = c.Controller()
        # self.file_name = input("Please enter the file name")
        # self.im_name = input("Please enter the image name or enter to use default image")
        self.file_name = "data/fixed.csv"
        self.im_name = "data/paths0.png"
        if not self.im_name:
            self.im_name = "data/paths0.png"
        try:
            self.cone.read_data(self.file_name)
        except:
            print("Can't read the file")
        try:
            self.cone.read_image(self.im_name)
        except:
            print("Can't read the image")

        # self.cone.draw_paths(self.cone.df.h)


    def switch_cases(self):
        x = None
        while( x is None and x != '-1'):

           filters = {
               '-1': self.cone.exit,
               '1': self.cone.rap_filter_by_time,
               '2': self.cone.rap_filter_by_date_time,
               '3': self.cone.rap_filter_by_chossen_squere,
               '4': self.cone.rap_filter_by_area,
               # 5: 'paths per location, date and time'
           }
           msg = """
                       1: paths by time
                       2: paths by date and time
                       3: paths per chosen square location
                       4: paths per location
             
                       
                       to exit press -1
                   """

           inp = input(f'to choose your filter press :{msg}\n ')
           x = inp
        return filters[x]











