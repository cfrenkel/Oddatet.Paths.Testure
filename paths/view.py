import matplotlib.image as im
import matplotlib.pyplot as plt
import pandas as pd
import datetime
from PIL import Image

class View:

    def read_data(self,name):
        col_names = ["frame", "x", "y", "obj", "size", "seq", "tbd1", "tbd2", "tbd3", "filename", "time", "path_time",
                     "delta_time", "tbd4"]
        use_cols = ["x", "y", "obj", "size", "seq", "filename", "time", "delta_time"]
        df = pd.read_csv(name, names=col_names, usecols=use_cols, parse_dates=['time'],
                         infer_datetime_format=True)
        df['time'] = df['time'] + pd.to_timedelta(df['delta_time'])
        df = df.drop(['delta_time'], axis=1)
        gl_int = df.select_dtypes(include=['int64'])
        converted_int = gl_int.apply(pd.to_numeric, downcast='unsigned')
        df[converted_int.columns] = converted_int
        # gl_obj = df.select_dtypes(include=['object']).copy()
        # converted_obj = pd.DataFrame()
        #
        # for col in gl_obj.columns:
        #     num_unique_values = len(gl_obj[col].unique())
        #     num_total_values = len(gl_obj[col])
        #     if num_unique_values / num_total_values < 0.5:
        #         converted_obj.loc[:, col] = gl_obj[col].astype('category')
        #     else:
        #         converted_obj.loc[:, col] = gl_obj[col]
        #
        # compare_obj = pd.concat([gl_obj.dtypes, converted_obj.dtypes], axis=1)
        # compare_obj.columns = ['before', 'after']
        # compare_obj.apply(pd.Series.value_counts)
        # df[converted_obj.columns] = converted_obj
        df.to_pickle("data/pickle.pkl.xz")
        self.df = pd.read_pickle("data/pickle.pkl.xz")


    def read_image(self,name):
        file = Image.open(name)
        self.image = file

    def draw_paths(self):
        d = self.df.groupby(['obj','filename']).size().sample(20)
        df_by_obj = self.df.set_index(['obj', 'filename']).sort_index()
        plt.imshow(self.image)
        for r in d.index:
            oo = df_by_obj.loc[r]
            plt.plot(oo.x, oo.y)
        plt.show()

    def __init__(self):
        self.file_name = input("Please enter the file name")
        self.im_name = input("Please enter the image name or enter to use default image")
        if not self.im_name:
            self.im_name = "data/paths0.png"
        try:
            self.read_data(self.file_name)
        except:
            print("Can't read the file")
        try:
            self.read_image(self.im_name)
        except:
            print("Can't read the image")
        self.draw_paths()


        print(self.df.head(10))







