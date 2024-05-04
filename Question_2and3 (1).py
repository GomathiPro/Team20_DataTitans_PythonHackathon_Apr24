#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Question 2 : Divide GCS scores into slabs of 5 and count the number of patients under each band of score. Show this as any graph of your choice
#Divide GCS scores into slabs of 5 and count the number of patients under each band of score. Show this as any graph of your choice


# In[30]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


# question 2
df= pd.read_excel("G:\\My Drive\\JayanthiG\\Numpy_Ninja\\\Python\Python_Hackathon_Apr24\Cardiac_Outcomes.xlsx", sheet_name="Responsivenes")


# In[56]:


#GCS scores of patients
#Glasgow Coma Scale (GCS) is used to objectively describe the extent of impaired consciousness in all types of acute medical and trauma patients.


# Create a pandas DataFrame
df = pd.DataFrame({'GCS Score': gcs_scores})

# Group the GCS scores into slabs of 5 and count the number of patients under each band of score
df['GCS Band'] = pd.cut(df['GCS Score'], bins=range(0, 16, 5), right=False)
patient_count = df['GCS Band'].value_counts().sort_index()

# Plot a bar graph
plt.bar(patient_count.index.astype(str), patient_count.values, color='skyblue')
plt.xlabel('GCS Score Bands')
plt.ylabel('Number of Patients')
plt.title('Number of Patients by GCS Score Bands')
plt.show()


# In[ ]:


#Add a calculated column called Discharge date into the Hospitalization_Discharge using the information already available to you


# In[68]:


# question 3
df= pd.read_excel("G:\\My Drive\\JayanthiG\\Numpy_Ninja\\\Python\Python_Hackathon_Apr24\Cardiac_Outcomes.xlsx", sheet_name="Hospitalization_Discharge")
Hospitalization_Discharge = pd.DataFrame(df)
# Convert 'Admission Date' to datetime format
Hospitalization_Discharge['Admission_date'] = pd.to_datetime(Hospitalization_Discharge["Admission_date"])

# Calculate 'Discharge Date' based on 'Admission Date' and 'dischargeDay'
Hospitalization_Discharge['Discharge Date'] = Hospitalization_Discharge["Admission_date"] + pd.to_timedelta(Hospitalization_Discharge["dischargeDay"], unit='D')

# Display the updated dataframe with the calculated 'Discharge Date' column
print(Hospitalization_Discharge)


# In[ ]:


#question :What is the ratio of patients who were responsive to pain vs responsive to sound?

