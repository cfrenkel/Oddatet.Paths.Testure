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





if __name__ == '__main__':
    unittest.main()