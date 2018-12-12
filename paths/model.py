import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path


class Model:

    def __init__(self):
        pass

    def read_data(self,name):
        new_name = name[:name.find('.')] + ".pkl.xz"
        file = Path(new_name)
        if not file.exists():
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

            df.to_pickle(new_name)
        self.df = pd.read_pickle(new_name)
        self.df_by_obj = self.df.set_index(['obj', 'filename']).sort_index()
        self.filter_req = self.df

    def read_image(self,name):
       file = plt.imread(name)
       self.image = file
       self.name = name
