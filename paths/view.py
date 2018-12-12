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

        self.cone.draw_paths()


    def switch_cases(self):
        x = None

        while(x is None):

           filters = {
               1: 'paths by time',
               2: 'paths by date and time',
               3: 'paths per location',
               4: 'paths per location and time',
               5: 'paths per location, date and time'
           }
           msg = """
                       1: paths by time
                       2: paths by date and time
                       3: paths per location
                       4: paths per location and time
                       5: paths per location, date and time
                   """

           inp = input(f'to choose your filter press :{msg}\n ')
           x = filters.get(inp)
        return filters[x]











