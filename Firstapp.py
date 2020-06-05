# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

st.title('Data-driven Soccer Betting')

st.write('Matchday 28:')
st.write('Bookmaker Odds:')
df=pd.read_csv('Betdata27.csv')
st.write(df[['Fixture:','Home win odds','Draw odds','Away win odds']])

option = st.selectbox(
    'Which match would you like to bet on?',
     df['Fixture:'])

df2=df[['Home Team','Away Team','Draw option']].loc[df['Fixture:']==option]
#df2

option_team = st.selectbox(
    'Which team would you like to bet on?',
     (df2.iloc[0,0],df2.iloc[0,1],df2.iloc[0,2]))

d = {'Money': [10, 20, 50, 100]}
Betopt= pd.DataFrame(data=d)
 
#option1 = st.selectbox(
 #   'How much would you like to bet?',
  #   Betopt['Money'])
option1 = st.slider('How much would you like to bet?', 0, 200, 0)

#'You selected to bet', option1,'dollars on',option_team,'.'
if option1 != 0:
    if df2.iloc[0,0]==option_team:
        a1=df[['Home win odds']].loc[df['Fixture:']==option]
        t1=a1.iloc[0,0]
        
        b1=df[['Home win']].loc[df['Fixture:']==option]*100
        t2=b1.iloc[0,0]
        money=(t1-1)*option1
        
        'You have a '+str(round(t2,2))+'% chance of winning '+str(round(money,2))+' dollars.'
    elif df2.iloc[0,1]==option_team:
        a1=df[['Away win odds']].loc[df['Fixture:']==option]
        t1=a1.iloc[0,0]
        
        b1=df[['Away Win']].loc[df['Fixture:']==option]*100
        t2=b1.iloc[0,0]
        money=(t1-1)*option1
        
        'You have a '+str(round(t2,2))+'% chance of winning '+str(round(money,2))+' dollars.'
    else:
        a1=df[['Draw odds']].loc[df['Fixture:']==option]
        t1=a1.iloc[0,0]
        
        b1=df[['Draw']].loc[df['Fixture:']==option]*100
        t2=b1.iloc[0,0]
        money=(t1-1)*option1
        
        'You have a '+str(round(t2,2))+'% chance of winning '+str(round(money,2))+' dollars.'