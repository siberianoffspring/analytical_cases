import pandas as pd
import seaborn as sns
import matplotlib as mp
import numpy as np
from numpy import median

df = pd.read_excel('/Users/siberianoffspring/Desktop/it_spec/it_dataframe.xlsx')



df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ','_')

df = df.query('age >= 18 & age <= 60 ')


df['age_group'] = np.where((df['age']>=18) & (df['age']<24), '18-24', 
                  np.where((df['age']>=25) & (df['age']<35), '25-34', 
                  np.where((df['age']>=35) & (df['age']<50), '35-49', '50+')))

df_ages = df.groupby(['age_group'], as_index = False)\
            .agg({'id':'count'})\
            .rename(columns = {'id':'count_id'})

df_sex = df.groupby(['sex'], as_index = False)\
            .agg({'id':'count'})\
            .rename(columns = {'id':'count_id'})

df_ages['part_count'] = (df_ages.count_id / df_ages.count_id.sum()) * 100

df_ages = df_ages.round(0)

df_sex
