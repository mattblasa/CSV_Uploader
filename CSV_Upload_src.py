import pandas as pd 
import numpy as np
import os 
from sqlalchemy import create_engine

#create a dataframe
df = pd.read_csv("test,csv", encoding ='utf8')

#create an engine 
engine = create_engine('postgresql://postgres:noyS9oud!@localhost:5432/dbo.examples.marketing_practice')

df.to_sql('Table Name Test', engine, index=False)