import paths.controller as c

class View:

    def __init__(self):
      self.load()

    def load(self):
        # self.file_name = input("Please enter the file name")
        # self.im_name = input("Please enter the image name or enter to use default image")
        self.file_name = "data/fixed.csv"
        self.im_name = "data/paths0.png"
        if not self.im_name:
            self.im_name = "data/paths0.png"
        self.cone = c.Controller(self.file_name, self.im_name)

    def run(self):
        x = 100
        while (x != -1):
            x = self.switch_cases()
            x = x()


    def switch_cases(self):
        x = None
        while( x is None and x != '-1'):

           filters = {
               '-1': self.cone.exit,
               '1': self.cone.rap_filter_by_time,
               '2': self.cone.rap_filter_by_date_time,
               '3': self.cone.rap_filter_by_chossen_squere,
               '4': self.cone.rap_filter_by_area,
               '5': self.cone.rap_filter_by_time_chossen_squere,
               '6': self.cone.rap_filter_by_date_time_chossen_squere,
           }
           msg = """
                       1: paths by time
                       2: paths by date and time
                       3: paths per chosen square location
                       4: paths per location
                       5: paths per time and location
                       6: paths per date,time and location

                       to exit press -1
                   """

           inp = input(f'to choose your filter press :{msg}\n ')
           x = inp

           try:
             filters[x]
           except:
               print("Enter a valid key!!!\n")
               return self.switch_cases()

        return filters[x]











