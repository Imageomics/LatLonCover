import unittest
from unittest.mock import patch, Mock
import pandas as pd
from latloncover.classify import add_classifications

CROPSPACE_XML = """
<data>
  <returnURL>someurl</returnURL>
</data>
"""

CROPSPACE_CSV = """Value, Category, Count,  Acreage
1, Corn, 10, 1.0
27, Rye, 1, 1.0
111, Open Water, 42, 1.0
121, Developed/Open Space, 1835, 2.0
131, Barren, 12, 3.0
141, Deciduous Forest, 4464, 2.0
190, Woody Wetlands, 1635, 10.0
"""


class TestLatLonCov(unittest.TestCase):
    @patch('latloncover.classify.requests')
    def test_add_classifications(self, mock_requests):
         # returns XML with URL simulating cropspace first response
        mock_requests.post.return_value = Mock(text=CROPSPACE_XML)
        # returns CSV with simulating cropspace second response
        mock_requests.get.return_value = Mock(text=CROPSPACE_CSV)

        data = [
            (36.001465, -78.939133),
        ]
        df = pd.DataFrame(data, columns=['lat', 'lon'])
        
        result = add_classifications(df, lat_col='lat', lon_col='lon')

        expected_columns = [
            'lat', 'lon', 'bb_small', 'bb_big', 
            'A_small', 'B_small', 'D_small', 'F_small', 'G_small',
            'N_small', 'W_small', 'WL_small', 'A_big', 'B_big',
            'D_big', 'F_big', 'G_big', 'N_big', 'W_big', 'WL_big'
        ]
        self.assertEqual(result.columns.to_list(), expected_columns)
        # The cropspace CSV literal above has 50% wetlands
        self.assertEqual(result['WL_small'].to_list(), [0.5])
        # Same value for big since mock_requests.get always returns the same value
        self.assertEqual(result['WL_big'].to_list(), [0.5])
        
        # The cropspace CSV literal above has 10% developed
        self.assertEqual(result['D_small'].to_list(), [0.1])
        # Same value for big since mock_requests.get always returns the same value
        self.assertEqual(result['D_big'].to_list(), [0.1])
