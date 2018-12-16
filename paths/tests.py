import pandas as pd
import unittest

from paths.controller import Controller

class SimpleTests(unittest.TestCase):
    def setUp(self):
        self.file_name = "data/fixed.csv"
        self.image ="data/paths0.png"
        self.test_df = pd.read_pickle('C:/Users/RENT/Desktop/xt-paths-research-ella-team-2-chani-orly-elisheva/data/fixed.pkl.xz')
        self.con = Controller(self.file_name,self.image)
        self.con.m.read_image('C:/Users/RENT/Desktop/xt-paths-research-ella-team-2-chani-orly-elisheva/data/paths0.png')

    def test_filter_by_time(self):
        self.assertEqual(len(self.con.filter_by_time(self.test_df,'01:27:09','01:28:17')),8)

    def test_false_filter_by_time(self):
        self.assertNotEqual(len(self.con.filter_by_time(self.test_df,'01:27:09','01:28:17')),20)

    def test_filter_by_date_time(self):
        self.assertEqual(len(self.con.filter_by_date_time(self.test_df, '2017-08-20 00:01:21', '2017-08-20 00:02:05')), 8)

    def test_false_filter_by_date_time(self):
        self.assertNotEqual(len(self.con.filter_by_date_time(self.test_df, '2017-08-20 00:01:21', '2017-08-20 00:02:05')), 24)

    def test_filter_by_area(self):
        self.assertEqual(len(self.con.filter_by_area(self.test_df,0,0,5,5)),24)

    def test_false_filter_by_area(self):
        self.assertNotEqual(len(self.con.filter_by_area(self.test_df, 0, 0, 5, 5)), 8)

    # def test_filter_by_chossen_squere(self):
    #     self.assertEqual(len(self.con.filter_by_chossen_squere(self.test_df,'5')),1)
    #

    # def test_filter_by_time_chossen_squere(self):
    #
    #
    # def rap_filter_by_date_time_chossen_squere(self):
# class FiltersTestCase(unittest.TestCase):
#
#     def setUp(self):
#         self.df = pd.read_pickle('data/fixed.pkl.xz').head(20)
#         self.im = plt.imread("data/paths0.png")
#
#
#
#
#     ############################test ones filter########################################
#
#
#     def test_area(self):
#         x1 = '0'
#         y1 = '0'
#         x2 = "5"
#         y2 = "150"
#
#         df2 = square_filter(self.df, x1, y1, x2, y2)
#         self.assertEqual(1, len(df2))
#
#     def test_few_squers(self):
#
#         args = ['(0,2)']
#
#         df2 = few_square_filter(self.df, args, self.im)
#         self.assertEqual(1, len(df2))
#
#     def test_date_filter(self):
#         args = ['2017-08-17','01:27:10','2017-08-17','01:28:18']
#         df2 = time_in_one_day_filter(self.df, args[0] + " " + args[1], args[2] + " " + args[3])
#         self.assertEqual(3, len(df2))
#
#     def test_time_filter(self):
#
#         start_time = "01:27:09"
#         end_time = "01:28:17"
#         df2 = time_in_all_day_filter(self.df, start_time, end_time)
#         self.assertEqual(6, len(df2))
#
#     # ############################test combination tow filters########################################
#
#     def test_time_filter_and_date_filter(self):
#         args = ['2017-08-17', '01:27:10', '2017-08-17', '01:28:18']
#         df2 = time_in_one_day_filter(self.df, args[0] + " " + args[1], args[2] + " " + args[3])
#         start_time = "01:27:09"
#         end_time = "01:28:17"
#         df3 = time_in_all_day_filter(df2, start_time, end_time)
#         self.assertEqual(1, len(df3))
#
#
#
#     def test_time_filter_and_squers_filter(self):
#         args = ['(0,2)']
#
#         df2 = few_square_filter(self.df, args, self.im)
#         start_time = "01:27:09"
#         end_time = "01:28:17"
#         df3 = time_in_all_day_filter(df2, start_time, end_time)
#         self.assertEqual(1, len(df3))
#
#
#     def test_time_filter_and_area_filter(self):
#         #time_filter
#         start_time = pd.to_datetime("01:27:09")
#         end_time = pd.to_datetime("01:28:18")
#         df2 = time_in_all_day_filter(self.df, start_time, end_time)
#
#         #area_filter
#         x1 = "75"
#         y1 = "99"
#         x2 = "639"
#         y2 = "350"
#
#         df3 = square_filter(df2, x1, y1, x2, y2)
#         self.assertEqual(2, len(df3))
#
#     def test_date_filter_and_squers_filter(self):
#
#         #date_filter
#         args = ['2017-08-17', '01:27:10', '2017-08-17', '01:28:18']
#         df2 = time_in_one_day_filter(self.df, args[0] + " " + args[1], args[2] + " " + args[3])
#
#         #squers_filter
#         args = ['(0,2)']
#         df3 = few_square_filter(df2, args, self.im)
#
#         self.assertEqual(0, len(df3))
#
#     def test_date_filter_and_test_area_filter(self):
#         # date_filter
#         args = ['2017-08-17', '01:27:10', '2017-08-17', '01:28:18']
#         df2 = time_in_one_day_filter(self.df, args[0] + " " + args[1], args[2] + " " + args[3])
#
#         #test_area_filter
#         x1 = "75"
#         y1 = "99"
#         x2 = "639"
#         y2 = "350"
#
#         df3 = square_filter(df2, x1, y1, x2, y2)
#         self.assertEqual(2, len(df3))
#
#     def test_squers_filter_and_test_area_filter(self):
#
#         #squers_filter
#
#         args = ['(1,9)','(9,9)']
#         df2 = few_square_filter(self.df, args, self.im)
#
#         x1 = "75"
#         y1 = "99"
#         x2 = "639"
#         y2 = "350"
#
#         #area_filter
#
#         df3 = square_filter(df2, x1, y1, x2, y2)
#         self.assertEqual(0, len(df3))




if __name__ == '__main__':
    unittest.main()