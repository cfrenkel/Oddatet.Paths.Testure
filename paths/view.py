import matplotlib.pyplot as plt
import pandas as pd
import paths.controller as c

class View:

    def __init__(self):
        self.cone = c.Controller()
        self.file_name = input("Please enter the file name")
        self.im_name = input("Please enter the image name or enter to use default image")
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









