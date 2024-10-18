'''
Created on Oct 18, 2024

@author: neda
'''
import unittest
import paraBozdur as pb


class Test(unittest.TestCase):


    def testParaBozdurWithBanknot(self):
        self.assertListEqual([0,0,1,0,0,0,0,0], pb.paraBozdur(5))


