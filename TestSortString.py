import unittest
import os
from SortString import SortStringObject

class TestSortString(unittest.TestCase):
    def test_sort(self):
        #mystring = ['portland','corvallis','seattle','Washington','Anaheim']
        mystring = 'portland,corvallis,seattle,Washington,Anaheim'
        obj = SortStringObject()
        obj.write_to_file('testinput.csv', mystring)
        self.assertEquals(os.path.exists('.\\testinput.csv'), True)
        obj.write_to_file('testoutput.csv', obj.read_from_file('input.csv'))



if __name__ == '__main__':
    unittest.main()
