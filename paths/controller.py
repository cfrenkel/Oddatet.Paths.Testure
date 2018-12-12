import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
from paths.model import Model

class Controller:
    def __init__(self,fn,im):
        self.m = Model()
        self.m.read_data(fn)
        self.m.read_image(im)


    def draw_paths(self, d):
          self.m.image = plt.imread(self.m.name)
          pa = d.groupby(['obj', 'filename']).size()
          plt.imshow(self.m.image)
          # if(len(pa) <= 200):
          #     for r in pa.index:
          #         oo = self.df_by_obj.loc[r]
          #         plt.subplot(oo.x, oo.y)
          # else:
          for r in pa.index:
              oo = self.m.df_by_obj.loc[r]
              plt.plot(oo.x, oo.y)

          plt.show()

    def filter_by_date_time(self, d,b1, b2):

        b1 = pd.to_datetime(b1)
        b2 = pd.to_datetime(b2)

        time_tf = d[(d.time.between(b1, b2))]
        t = time_tf.drop_duplicates(['obj', 'filename'])

        return t

    def filter_by_time(self,d, b1, b2):
        b1 = pd.to_datetime(b1).time()
        b2 = pd.to_datetime(b2).time()

        time_tf = d[(d.time.dt.time.between(b1, b2))]
        t = time_tf.drop_duplicates(['obj', 'filename'])

        return t

    def filter_by_area(self,d, x1,y1,x2,y2):
        loc_so = d[(d.x.between(x1, x2)) & (d.y.between(y1, y2))]
        top = loc_so.drop_duplicates(['obj', 'filename'])

        return top

    def filter_by_chossen_squere(self,d, x, y):

        width = self.m.image.shape[1]
        height = self.m.image.shape[0]
        num_segmentation = 10
        r = int(x)
        c = int(y)
        top_left = (c * width / num_segmentation, (r + 1) * height / num_segmentation)
        bottom_right = ((c + 1) * width / num_segmentation, r * height / num_segmentation)
        return self.filter_by_area(d,top_left[0],bottom_right[1],bottom_right[0],top_left[1])

    def rap_filter_by_time(self):
        q = input("Do you want to refresh the data y/n?")
        if q == 'y':
           self.m.filter_req = self.m.df
        t1 = input('enter first range of time in format hh:mm:ss\n')
        t2 = input('enter last range of time in format hh:mm:ss\n')

        self.m.filter_req = self.filter_by_time(self.m.filter_req,t1,t2)
        self.draw_paths(self.m.filter_req)
        return


    def rap_filter_by_date_time(self):
        q = input("Do you want to refresh the data y/n?")
        if q == 'y':
            self.m.filter_req = self.m.df
        t1 = input('enter first range of time in format yyyy-mm-dd hh:mm:ss\n')
        t2 = input('enter last range of time in format yyyy-mm-dd hh:mm:ss\n')

        self.m.filter_req = self.filter_by_date_time(self.m.filter_req, t1, t2)
        self.draw_paths(self.m.filter_req)
        return

    def draw_grid(self):
        img = self.m.image
        for i in range(50, 1000, 50):
            img[i:i + 5, :] = 0
            img[:, i:i + 5] = 0

        plt.imshow(img)
        plt.show()
        # plt.imshow(img)
        plt.close()

    def rap_filter_by_chossen_squere(self):
        q = input("Do you want to refresh the data y/n?")
        if q == 'y':
            self.m.filter_req = self.m.df
        elif q == 'n':
            self.m.filter_req = self.m.filter_req
        self.draw_grid()

        x = input('enter x of wanted square (top left pixel)\n')
        y = input('enter y of wanted square (top left pixel)\n')

        self.m.filter_req = self.filter_by_chossen_squere(self.m.filter_req, x, y)
        self.draw_paths(self.m.filter_req)
        return

    def rap_filter_by_area(self):
        q = input("Do you want to refresh the data y/n?")
        if q == 'y':
            self.m.filter_req = self.m.df
        elif q == 'n':
            self.m.filter_req = self.m.filter_req
        self.draw_grid()

        x1 = input('enter x of wanted square (top left pixel)\n')
        y1 = input('enter y of wanted square (top left pixel)\n')
        x2 = input('enter x of wanted square (bottom left pixel)\n')
        y2 = input('enter y of wanted square (bottom left pixel)\n')

        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)



        self.m.filter_req = self.filter_by_area(self.m.filter_req, x1, y1, x2,y2)
        self.draw_paths(self.m.filter_req)
        return

    def exit(self):
        print("👋👋👋 Goodbye 👋👋👋")
        return -1








