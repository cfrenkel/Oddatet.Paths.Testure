import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as plticker


from paths.model import Model

class Controller:

    def __init__(self, fn, im):
        self.m = Model()
        try:
            self.m.read_data(fn)
        except:
            print("Can't read the file :( \n")
            exit()
        try:
            self.m.read_image(im)
        except:
            print("Can't read the image :( \n")
            exit()

    def draw_paths(self, d):
            pa = d.groupby(['obj', 'filename']).size()
            self.m.image = plt.imread(self.m.name)
            # plt.imshow(self.m.image)
            # if len(pa) <= 11:
            #     if self.ans():
            #         for t in pa.index:
            #             oo = self.m.df_by_obj.loc[t]
            #             plt.imshow(self.m.image)
            #             plt.plot(oo.x, oo.y)
            #             plt.pause(0.1)
            #             plt.gcf().clear()
            #     else:
            #         for t in pa.index:
            #             oo = self.m.df_by_obj.loc[t]
            #             plt.imshow(self.m.image)
            #             plt.plot(oo.x, oo.y)
            #         plt.pause(0.1)
            #         plt.gcf().clear()
            # else:
            for t in pa.index:
                oo = self.m.df_by_obj.loc[t]
                plt.plot(oo.x, oo.y)
                #plt.pause(0.1)
            plt.imshow(self.m.image)
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

    def filter_by_chossen_squere(self, d, location_list):

        width = self.m.image.shape[1]
        height = self.m.image.shape[0]
        num_segmentation = 10
        use_cols = ["x", "y", "obj", "size", "seq", "filename", "time"]
        t = pd.DataFrame([], columns=use_cols)
        for i in location_list:
            r = i[1]
            c = i[0]
            top_left = (c * width / num_segmentation, (r + 1) * height / num_segmentation)
            bottom_right = ((c + 1) * width / num_segmentation, r * height / num_segmentation)
            t = t.append(self.filter_by_area(d, top_left[0], bottom_right[1], bottom_right[0], top_left[1]))
        return t

    def rap_filter_by_time(self, t1,t2, v):

        self.refresh_data(v)

        # t1 = input('enter first range of time in format hh:mm:ss\n')

        # try:
        #     pd.to_datetime(t1).time()
        # except:
        #     print("Invalid time :( \n")
        #     return
        # # t2 = input('enter last range of time in format hh:mm:ss\n')
        #
        # try:
        #     pd.to_datetime(t2).time()
        # except:
        #     print("Invalid time :( \n")
        #     return

        self.m.filter_req = self.filter_by_time(self.m.filter_req,t1,t2)
        # self.draw_paths(self.m.filter_req)
        return

    def rap_filter_by_date_time(self, t1, t2, v):

        self.refresh_data(v)
        # t1 = input('enter first range of time in format yyyy-mm-dd hh:mm:ss\n')
        try:
            pd.to_datetime(t1)
        except:
            print("Invalid date time :( \n")
            return
        # t2 = input('enter last range of time in format yyyy-mm-dd hh:mm:ss\n')
        try:
            pd.to_datetime(t2)
        except:
            print("Invalid date time :( \n")
            return

        self.m.filter_req = self.filter_by_date_time(self.m.filter_req, t1, t2)
        # self.draw_paths(self.m.filter_req)
        return

    def rap_filter_by_chossen_squere(self, l, v):

        self.refresh_data(v)
        # self.draw_grid()

        #l = input("Enter list of wanted square on the picture\n")
        l = l.split(" ")
        if self.cheak_list(l):
            self.m.filter_req = self.filter_by_chossen_squere(self.m.filter_req, self.calc_points(l))
            # self.draw_paths(self.m.filter_req)
        else:
            print("Invalid Input :(\n")
        return

    def rap_filter_by_area(self, x1, y1, x2, y2, v):
        self.refresh_data(v)
        # self.draw_grid()

        # x1 = input('enter x of wanted square (top left pixel)\n')
        # y1 = input('enter y of wanted square (top left pixel)\n')
        # x2 = input('enter x of wanted square (bottom left pixel)\n')
        # y2 = input('enter y of wanted square (bottom left pixel)\n')

        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)

        self.m.filter_req = self.filter_by_area(self.m.filter_req, x1, y1, x2,y2)
        # self.draw_paths(self.m.filter_req)
        return

    def rap_filter_by_time_chossen_squere(self, t1, t2, l, v):
        self.refresh_data(v)

        # t1 = input('enter first range of time in format yyyy-mm-dd hh:mm:ss\n')
        # t2 = input('enter last range of time in format yyyy-mm-dd hh:mm:ss\n')

        self.m.filter_req = self.filter_by_time(self.m.filter_req, t1, t2)

        print("Good now choose your squares\n")
        # self.draw_grid()

        # l = input("Enter list of wanted square on the picture\n")
        l = l.split(" ")
        self.m.filter_req = self.filter_by_chossen_squere(self.m.filter_req, self.calc_points(l))
        # self.draw_paths(self.m.filter_req)

    def rap_filter_by_date_time_chossen_squere(self, t1, t2, l, v):

        self.refresh_data(v)

        # t1 = input('enter first range of time in format hh:mm:ss\n')
        # t2 = input('enter last range of time in format hh:mm:ss\n')

        self.m.filter_req = self.filter_by_date_time(self.m.filter_req, t1, t2)

        print("Good now choose your squares\n")
        self.draw_grid()

        # l = input("Enter list of wanted square on the picture\n")
        l = l.split(" ")
        self.m.filter_req = self.filter_by_chossen_squere(self.m.filter_req, self.calc_points(l))
        self.draw_paths(self.m.filter_req)

    def draw_grid(self):

        # Load the image
        img = self.m.image
        imgh, imgw = img.shape[0], img.shape[1]
        fig = plt.figure(figsize=(15, 10))
        ax = fig.add_subplot(111)

        myInterval_w = imgw // 10
        myInterval_h = imgh // 10

        loc_w = plticker.MultipleLocator(base=myInterval_w)
        loc_h = plticker.MultipleLocator(base=myInterval_h)

        ax.xaxis.set_major_locator(loc_w)
        ax.yaxis.set_major_locator(loc_h)

        # Add the grid
        ax.grid(which='major', axis='both', linestyle='-', color="k")

        # Add the image
        ax.imshow(img)

        # Find number of gridsquares in x and y direction
        nx = abs(int(float(ax.get_xlim()[1] - ax.get_xlim()[0]) / float(myInterval_w)))
        ny = abs(int(float(ax.get_ylim()[1] - ax.get_ylim()[0]) / float(myInterval_h)))

        # Add some labels to the gridsquares
        for j in range(ny):
            y = myInterval_h / 2 + j * myInterval_h
            for i in range(nx):
                x = myInterval_w / 2. + float(i) * myInterval_w
                ax.text(x, y, '{:d}'.format(i + j * nx), color='w', ha='center', va='center')

        # Show the result
        plt.imshow(img)
        plt.show()

    def refresh_data(self, v):

        # q = None
        # while q!= 'y' or q!='n':
        #     q = input("Do you want to refresh the data [y/n]?")
        if v:
            self.m.filter_req = self.m.df
        else:
            self.m.filter_req = self.m.filter_req

    def ans(self):
        q = None
        while q != 'y' or q != 'n':
            q = input("Do you want to see every picture separate[y/n]?\n")
            if q == 'y':
                return True
            elif q == 'n':
                return False
            else:
                print("Invalid answer :(")

    def exit(self):
        print("👋👋👋 Goodbye 👋👋👋")
        return -1

    def cheak_list(self, l):
        for i in l:
            try:
                i = int(i)
            except:
                return False
        return True

    def calc_points(self, l):
        points = []
        re = {}
        for i in range(0,10):
            for j in range(0,10):
                points.append((i, j))
        for i in range(0, 100):
            re[str(i)] = points[i]

        tup_list = []
        for i in l:
            tup_list.append(re[i])

        return tup_list





