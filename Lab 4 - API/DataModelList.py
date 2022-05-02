# -*- coding: utf-8 -*-
"""
Created on Sun May  1 18:02:24 2022

@author: Carlos Silva, Sara Calle, Juliana Velasco
"""


from pydantic import BaseModel
from typing import Optional, List
from DataModelLifeExpectancy import DataModelLifeExpectancy

class DataModelList(BaseModel):

# Estas varibles permiten que la librería pydantic haga el parseo entre el Json recibido y el modelo declarado.
    datos: Optional[List[DataModelLifeExpectancy]]
