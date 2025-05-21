#!/usr/bin/env python
# coding: utf-8

# In[3]:


#loading the dataset and checking the entire values
import pandas as pd
df=pd.read_csv('hospital_patient_records.csv')
print(df.to_string())


# In[9]:


df.head(500)


# In[4]:


#checking the number of columns, entries , and data type
df.info()


# In[5]:


#checking the number of rows specifically to focus on the size of dataset
df.shape[0]


# In[6]:


#checking the null values and count of that
df.isnull().sum()


# In[10]:


df['Length of Stay']


# In[11]:


#checking the null values in the column "length of stay"
df['Length of Stay'].isnull()


# In[12]:


#retrieved just the null values
df[df['Length of Stay'].isnull()]


# In[13]:


#checking min, max, and average to see outliers and options for filling null values
max_value=df['Length of Stay'].max()
min_value=df['Length of Stay'].min()
avg_value=df['Length of Stay'].mean()
print("Max:", max_value)
print("Min:", min_value)
print("Average:", avg_value)


# In[14]:


#checking the skewness of data in that column to select the best way for filling missing values
df['Length of Stay'].hist(bins=20)


# In[16]:


# selected the median as the best approach due to uniform data and safeside from high gap in values for future
x=df['Length of Stay'].median()
df['Length of Stay'].fillna(x, inplace=True)
df


# In[18]:


#all null values handled in length of stay column
df['Length of Stay'].isnull().sum()


# In[19]:


#focused on null values for Treatment Cost column
df[df['Treatment Cost'].isnull()]


# In[20]:


#dropped the null values of treatment cost column
df.dropna(subset=['Treatment Cost'], inplace=True)
df


# In[21]:


#checked for the null values in treatment cost column
df.isnull().sum()


# In[22]:


df['Doctor Name'].fillna('Unknown', inplace=True)
df


# In[32]:


df['Admission Date'] = pd.to_datetime(df['Admission Date'])
df['Discharge Date'] = pd.to_datetime(df['Discharge Date'])


# In[25]:


#data analysis
#1.Find the average Length of Stay per department.
df.groupby('Department')['Length of Stay'].mean().round(2).sort_values(ascending=False)


# In[ ]:


#<<<<<Neurology taking maximum avg time and Cardiology min avg time>>>>


# In[27]:


# 2. Calculate total and average treatment cost by gender
df.groupby('Gender')['Treatment Cost'].agg(['sum','mean'])


# In[29]:


# 3.Find top 3 most common diagnoses
df['Diagnosis'].value_counts().head(3)


# In[38]:


#4.Count patients admitted in each month
df['Month']=df['Admission Date'].dt.month_name()
df['Month'].value_counts().sort_index()


# In[40]:


#5. Group by Department and calculate:Total cost of treatments
df.groupby('Department')['Treatment Cost'].mean().round(2).sort_values(ascending=False)


# In[41]:


#6.List patients whose Treatment Cost is above the 90th percentile.
pctl=df['Treatment Cost'].quantile(0.90)
df1=df[df['Treatment Cost']>pctl]
df1


# In[42]:


#7. Sort patients by Length of Stay in descending order
df.sort_values(by='Length of Stay', ascending=False)


# In[43]:


#8.Create a new column: Out_of_Pocket = Treatment Cost - Insurance Covered
df['Out_of_pocket']=df['Treatment Cost']-df['Insurance Covered']
df


# In[44]:


#9.Create another column: Age Group (e.g., <18, 18-35, 36-60, 60+)
def get_age_group(Age):
    if Age<18:
        return 'child'
    elif 18<=Age<=35:
        return ' young adult'
    elif 36<=Age<=60:
        return 'adult'
    else:
        return 'senior'
df['Age_group']=df['Age'].apply(get_age_group)


# In[45]:


df


# In[46]:


df.to_csv('C:/Users/kamal/Downloads/analyzed_hospital records.csv', index=False)


# In[ ]:




