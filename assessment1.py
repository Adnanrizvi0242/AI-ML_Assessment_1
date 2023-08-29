# -*- coding: utf-8 -*-
"""Assessment1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Laxtaos1yjXCSpI9mqpRmHafQ7lMpeyB
"""

import pandas as pd
import numpy as np

# creating a dictionary

dictionary = {'NAME': ['Adnan', 'Adam' , 'Aiyaz' , 'Saksham', 'Anirudh' , 'Gopal' , 'Sakwik', 'Monu' , 'Bunty', 'Bubly'], 'AGE': [25 , 28 , np.nan , 41, 18,41, 15,45,18,17],'STATE':['AP','UP','Goa','JH','Bihar','TN',np.nan,'UP','MP','JH'],'GENDER':['M','M','F','F','T','F','T','M','F','T'],'MOBILE':['Nokia','MI','Apple','Samsung','Redmi','Mi','Oneplus','Apple','Samsung','Oppo']}

"""# Create a pandas dataframe"""

# Create a pandas dataframe

df = pd.DataFrame(dictionary)

df

#Check the info of 'df'
df.info()

#Check the descriptive statistics of 'df'
df.describe()

#check the 4th index observation with 'loc' slicing operator.
df.loc[4]

#Check the null values in your 'df'
df.isnull()

df.isnull().any()

df.isnull().sum()

