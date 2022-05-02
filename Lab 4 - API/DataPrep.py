# -*- coding: utf-8 -*-
"""
Created on Sun May  1 15:37:01 2022

@author: cesl
"""
from sklearn.impute import SimpleImputer
import pandas as pd
import numpy as np

# Crear una funcion para quitar los atipicos del Income Comp
def IncomeCompOutliers(col):
    
    # Crear un Simple Imputer
    incomeComp_imp = SimpleImputer(strategy = 'mean')
 
    # Performing basic imputation for nulls
    imputed = incomeComp_imp.fit_transform(col)
    incomComp = pd.DataFrame(data = imputed, columns = ['Income composition of resources'])
 
    #5% inferior
    inf = incomComp['Income composition of resources'].quantile([.05])
    inf_val = inf.get(0.05)
    
    #5% superior
    sup = incomComp['Income composition of resources'].quantile([.95])
    sup_val = sup.get(0.95)

    # Arreglar los outliers inferiores
    incomComp['Income composition of resources'] = incomComp['Income composition of resources'].mask(incomComp['Income composition of resources'] < inf_val, np.nan)
    media = incomComp['Income composition of resources'].mean()
    incomComp['Income composition of resources'] = incomComp['Income composition of resources'].fillna(media)
    
    #Arreglar los outliers superiores
    incomComp['Income composition of resources'] = incomComp['Income composition of resources'].mask(incomComp['Income composition of resources'] > sup_val, np.nan)
    media = incomComp['Income composition of resources'].mean()
    incomComp['Income composition of resources'] = incomComp['Income composition of resources'].fillna(media)

 
    return incomComp


# Crear una funcion para quitar los atipicos del GDP
def GDPOutliers(col):
    
    # Crear un Simple Imputer
    gdp_imp = SimpleImputer(strategy = 'mean')
 
    # Performing basic imputation for nulls
    imputed = gdp_imp.fit_transform(col)
    gdp = pd.DataFrame(data = imputed, columns = ['GDP'])
    
    #5% inferior
    inf = gdp['GDP'].quantile([.05])
    inf_val = inf.get(0.05)
    
    #5% superior
    sup = gdp['GDP'].quantile([.95])
    sup_val = sup.get(0.95)
    
    #Quitar parte inferior
    gdp['GDP'] = gdp['GDP'].mask(gdp['GDP'] < inf_val, inf_val)
    
    #Quitar parte superior
    gdp['GDP'] = gdp['GDP'].mask(gdp['GDP'] > sup_val, sup_val)
 
    return gdp


# Crear una funcion para quitar los atipicos del GDP
def BMIOutliers(col):
    
    # Crear un Simple Imputer
    bmi_imp = SimpleImputer(strategy = 'mean')
 
    # Performing basic imputation for nulls
    imputed = bmi_imp.fit_transform(col)
    bmi = pd.DataFrame(data = imputed, columns = ['BMI'])
    
    #5% inferior
    inf = bmi['BMI'].quantile([.05])
    inf_val = inf.get(0.05)
    
    #5% superior
    sup = bmi['BMI'].quantile([.95])
    sup_val = sup.get(0.95)
 
    # Quitar parte inferior
    bmi['BMI'] = bmi['BMI'].mask(bmi['BMI'] < inf_val, inf_val)
    
    # Quitar parte superior
    bmi['BMI'] = bmi['BMI'].mask(bmi['BMI'] > sup_val, sup_val)
 
    return bmi

# Crear una funcion para quitar los atipicos de HIV
def atipicosHIV(col):
    
    # Crear un Simple Imputer
    hiv_imp = SimpleImputer(strategy = 'mean')
 
    # Performing basic imputation for nulls
    imputed = hiv_imp.fit_transform(col)
    hiv_df = pd.DataFrame(data = imputed, columns = ['HIV/AIDS'])
 
    #5% inferior
    inf = hiv_df['HIV/AIDS'].quantile([.05])
    inf_val = inf.get(0.05)
    
    #5% superior
    sup = hiv_df['HIV/AIDS'].quantile([.95])
    sup_val = sup.get(0.95)

    # Arreglar los outliers inferiores
    hiv_df['HIV/AIDS'] = hiv_df['HIV/AIDS'].mask(hiv_df['HIV/AIDS'] < inf_val, np.nan)
    media = hiv_df['HIV/AIDS'].mean()
    hiv_df['HIV/AIDS'] = hiv_df['HIV/AIDS'].fillna(media)
    
    #Arreglar los outliers superiores
    hiv_df['HIV/AIDS'] = hiv_df['HIV/AIDS'].mask(hiv_df['HIV/AIDS'] > sup_val, np.nan)
    media = hiv_df['HIV/AIDS'].mean()
    hiv_df['HIV/AIDS'] = hiv_df['HIV/AIDS'].fillna(media)
    
 
    return hiv_df

# Crear una funcion para quitar los atipicos de adult mortality
def atipicosAdult(col):
    
    # Crear un Simple Imputer
    adult_imp = SimpleImputer(strategy = 'mean')
 
    # Performing basic imputation for nulls
    imputed = adult_imp.fit_transform(col)
    adult_imp = pd.DataFrame(data = imputed, columns = ['Adult Mortality'])
 
    #5% inferior
    inf = adult_imp['Adult Mortality'].quantile([.05])
    inf_val = inf.get(0.05)
    
    #5% superior
    sup = adult_imp['Adult Mortality'].quantile([.95])
    sup_val = sup.get(0.95)

    # Arreglar los outliers inferiores
    adult_imp['Adult Mortality'] = adult_imp['Adult Mortality'].mask(adult_imp['Adult Mortality'] < inf_val, np.nan)
    media = adult_imp['Adult Mortality'].mean()
    adult_imp['Adult Mortality'] = adult_imp['Adult Mortality'].fillna(media)
    
    #Arreglar los outliers superiores
    adult_imp['Adult Mortality'] = adult_imp['Adult Mortality'].mask(adult_imp['Adult Mortality'] > sup_val, np.nan)
    media = adult_imp['Adult Mortality'].mean()
    adult_imp['Adult Mortality'] = adult_imp['Adult Mortality'].fillna(media)
    
 
    return adult_imp