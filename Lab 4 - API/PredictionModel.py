# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 10:43:06 2022

@author: Carlos Silva, Sara Calle, Juliana Velasco
"""

from joblib import load

class Model:

    def __init__(self,columns):
        self.model = load("assets/modelo.joblib")

    def make_predictions(self, data):
        result = self.model.predict(data)
        return result
    
    