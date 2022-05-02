# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 10:19:12 2022

@author: Carlos Silva, Sara Calle, Juliana Velasco
"""

from fastapi import FastAPI
from DataModel import DataModel
from DataModelList import DataModelList
import pandas as pd
from joblib import load

app = FastAPI()


@app.get("/")
def read_root():
   return {"Hello": "World"}

@app.post("/predict")
def make_predictions(dataModel: DataModel):
    df = pd.DataFrame(dataModel.dict(), columns=dataModel.dict().keys(), index=[0])
    df.columns = dataModel.columns()
    model = load("assets/modelo.joblib")
    result = model.predict(df)
    result = result.tolist()
    return result

@app.post("/evaluate")
def evaluate_model(dataModelL: DataModelList):
    
    datosModelo = dataModelL.dict()['datos']
    columnas =  ["life_expectancy","Adult Mortality", "infant deaths", "Alcohol","percentage expenditure","Hepatitis B", "Measles", "BMI",
                "under-five deaths", "Polio", "Total expenditure", "Diphtheria", "HIV/AIDS", "GDP", "Population",
                "thinness 10-19 years", "thinness 5-9 years", "Income composition of resources", "Schooling"]
    
    df_temp = pd.DataFrame.from_dict(datosModelo, orient = "columns")
    df_temp.columns = columnas
    
    x = df_temp.drop("life_expectancy", axis = 1)
    y = df_temp["life_expectancy"]
    
    model = load("assets/modelo.joblib")
    result = model.score(x,y)
    result = str(result)
    return {"R^2" : result}
 

