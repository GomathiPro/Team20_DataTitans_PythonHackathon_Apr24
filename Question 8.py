#!/usr/bin/env python
# coding: utf-8

# In[18]:


# Q.8. Create a Waffle chart to show what percentage of total deaths belong to each admission_ward?import pandas as pd

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import openpyxl as xl
import pandas as pd
from pywaffle import Waffle


# In[4]:


Cardiac_outcomes=pd.ExcelFile(r"G:\\My Drive\\JayanthiG\Numpy_Ninja\\Python\\Python_Hackathon_Apr24\\Cardiac_Outcomes.xlsx")
Cardiac_outcomes.sheet_names


# In[95]:


df= Cardiac_outcomes.parse('Hospitalization_Discharge')
df.admission_ward.unique()
ward_grouping = {'Cardiology' : 'Cardiology','ICU': 'ICU','GeneralWard': 'GeneralWard','Others': 'Others'}
df['grouped_category'] = df['admission_ward'].map(ward_grouping).fillna(df['admission_ward'])
counts = df['grouped_category'].value_counts()
total_count = len(df['grouped_category'])
colors = {'Cardiology': '#2196f3',  
          'ICU': '#ff9800',   
          'GeneralWard': '#4caf50',  
          'Others': '#87CEFA'  
         }
df['percentage_death_within_28_days'] = (df['death_within_28_days'] / df['death_within_28_days'].sum()) * 100
df['percentage_deaths_3_months'] = (df['death_within_3_months'] / df['death_within_3_months'].sum()) * 100
df['percentage_death_within_6_months'] = (df['death_within_6_months'] / df['death_within_6_months'].sum()) * 100
df['percentage_deaths'] = df['percentage_death_within_28_days'] + df['percentage_deaths_3_months'] + df['percentage_death_within_6_months'] 
fig = plt.figure(
    FigureClass = Waffle,figsize=(5,8),
    rows=6,
    columns = 13,
    values=df['percentage_deaths'],
    title = {"label": "Total death percentage", "loc": "center", "size": 15},
    #labels=[f"{k} ({int(v / sum(data.values()) * 100)}%)" for k, v in df['grouped_category'] ],
    colors=[colors[category] for category in df['grouped_category']if category in colors],
    )
plt.legend(title='Legend',labels=[f"{k} (({v/total_count*100:.1f}%)" for k, v in counts.items()], loc='lower center', bbox_to_anchor=(0.5, -0.6))
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




