import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path


class Controller:
    def __init__(self):
        pass

    def read_data(self,name):
        new_name = name[:name.find('.')] + ".pkl.xz"
        file = Path(new_name)
        if not file.exists():
            print("in!!!")
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

    def read_image(self,name):
      file = plt.imread(name)
      self.image = file

    def draw_paths(self, d):
          d = d.groupby(['obj', 'filename']).size().sample(20)
          plt.imshow(self.image)
          for r in d.index:
              oo = self.df_by_obj.loc[r]
              plt.plot(oo.x, oo.y)
          plt.show()

    def filter_by_date_time(self, b1, b2):

        b1 = pd.to_datetime(b1)
        b2 = pd.to_datetime(b2)

        time_tf = self.df[(self.df.time.between(b1, b2))]
        t = time_tf.drop_duplicates(['obj', 'filename'])

        return t

    def filter_by_time(self, b1, b2):
        b1 = pd.to_datetime(b1).time()
        b2 = pd.to_datetime(b2).time()

        time_tf = self.df[(self.df.time.dt.time.between(b1, b2))]
        t = time_tf.drop_duplicates(['obj', 'filename'])

        return t

    def filter_by_area(self, x1,y1,x2,y2):
        loc_so = self.df[(self.df.x.between(x1, x2)) & (self.df.y.between(y1, y2))]
        top = loc_so.drop_duplicates(['obj', 'filename'])

        return top

    def filter_by_chossen_squere(self, x, y):
        width = self.image.size[1]
        height = self.image.size[0]
        num_segmentation = 10
        r = x
        c = y
        top_left = (c * width / num_segmentation, (r + 1) * height / num_segmentation)
        bottom_right = ((c + 1) * width / num_segmentation, r * height / num_segmentation)
        return self.filter_by_area(top_left[0],bottom_right[1],bottom_right[0],top_left[1])







