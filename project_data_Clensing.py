"""This program helps with data cleansing with the help of Numpy and Pandas"""

import pandas as pd
import numpy as np

df = pd.read_csv('ipl_initial_dataset.csv', header='infer')
df.info()
df.head()
data_csk = df.loc[(df["team1"]=="Chennai Super Kings") | (df["team2"]=="Chennai Super Kings") ]
data_csk.info()
csk_tosswin = df.loc[(df["toss_winner"]=="Chennai Super Kings")]
csk_tosswin.info()

csk_win = csk_tosswin.loc[(csk_tosswin["winner"]=="Chennai Super Kings")]
csk_win.info()

df['city'] = df['city'].fillna('Dubai')
df.drop(df.loc[df['result'] == 'no result'].index, inplace=True)
df.info()
df = df.drop(columns=['date','umpire1','umpire2','umpire3'])
df.head()
df.info()
df.to_csv("ipl_cleaned_data.csv")

