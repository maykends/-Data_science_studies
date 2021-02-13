# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 13:42:28 2021

@author: mayke
"""
# Pre-processamento de Dados

# Carregamento dos dados 
import pandas as pd
base = pd.read_csv("credit_data.csv")

base.describe()
