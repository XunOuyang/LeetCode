# -*- coding: utf-8 -*-
"""
Created on Sat May 19 20:30:17 2018

@author: tzlmyq
"""

class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        return rec1[0] < rec2[2] and rec1[2] > rec2[0] and rec1[3] > rec2[1] and rec1[1] < rec2[3]
