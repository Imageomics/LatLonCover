import unittest
import pandas as pd
from cover.LatLonConv import add_albers_bounding_boxes


class TestLatLonCov(unittest.TestCase):
    def test_add_albers_bounding_boxes(self):
        data = [
            (36.001465, -78.939133),
        ]
        df = pd.DataFrame(data, columns=['lat', 'lon'])
        add_albers_bounding_boxes(df, lat_column='lat', lon_column='lon')
        expected_bb_small = ['1515600.085597717,1574946.3607242196,1516404.7575977168,1575751.0327242194']
        self.assertEqual(df['bb_small'].to_list(), expected_bb_small)
        expected_bb_small = ['1514393.0815977168,1573739.3567242194,1517611.761597717,1576958.0367242196']
        self.assertEqual(df['bb_big'].to_list(), expected_bb_small)
