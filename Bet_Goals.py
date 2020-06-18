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
import altair as alt

st.title('Bet Goals')
st.write('Bet goals is an app designed to help you make informed bets on soccer matches')

st.subheader('Suggested Betting Strategy:') 
st.write('We suggest betting on games predicted by our model to end in a draw')

st.subheader('Rationale:') 
st.write('In the past 4 years, the bookmakers odds have always favoured either the home team or the away team. Not a single game has been backed by the bookmaker to end in a draw in this time frame. This systematic underestimation of the chances of a game ending in a draw lets the bookmaker overestimate the chances of a home win. To exploit this inefficiency, we built a model that can identify draws with 36% precision. Even though this means we will be wrong 2 out of 3 times, the odds on draws are have historically been high enough to give us around 20% return on investment.')

st.subheader('Matchday 28:')
st.subheader('Bookmaker Odds:')
df=pd.read_csv('Betdata27.csv')
st.write(df[['Fixture:','Home win odds','Draw odds','Away win odds','Predicted Result']])

#option = st.selectbox(
#    'Which match would you like to bet on?',
#     df['Fixture:'])


#df2

options_multi = st.multiselect('What fixtures would you like to bet on? (We suggest betting on games predicted to end in draws)', df['Fixture:'])

#st.write('You selected:', options_multi)

option_team=pd.DataFrame(columns=['Teamselected'])
option_amount=pd.DataFrame(columns=['Moneybet'])
option_poss_win=pd.DataFrame(columns=['Moneywon'])
option_prob_win=pd.DataFrame(columns=['Probwin'])

for i in range(len(options_multi)): 
    df2=df[['Home Team','Away Team','Draw option']].loc[df['Fixture:']==options_multi[i]]
    option_temp = st.selectbox(
        'Which team would you like to bet on in '+options_multi[i]+'?',
         (df2.iloc[0,0],df2.iloc[0,1],df2.iloc[0,2]))
    option_team=option_team.append({'Teamselected':option_temp}, ignore_index=True)    
#    option_team[['Teamselected']].iloc[i]=option_temp
    
    d = {'Money': [10, 20, 50, 100]}
    Betopt= pd.DataFrame(data=d)  
    widkey='slider'+str(i)
    option_mtemp = st.slider('How much would you like to bet?', 0, 200, 0, key=widkey)
    option_amount=option_amount.append({'Moneybet':option_mtemp}, ignore_index=True) 
    
    
    if df2.iloc[0,0]==option_temp:
        a1=df[['Home win odds']].loc[df['Fixture:']==options_multi[i]]
        t1=a1.iloc[0,0]
        
        b1=df[['Home win']].loc[df['Fixture:']==options_multi[i]]*100
        t2=b1.iloc[0,0]
        money=(t1-1)*option_mtemp
        
        option_poss_win=option_poss_win.append({'Moneywon': round(money,2)}, ignore_index=True)
        option_prob_win=option_prob_win.append({'Probwin': round(t2,2)/100}, ignore_index=True)
        if option_mtemp != 0:
            'You have a '+str(round(t2,2))+'% chance of winning '+str(round(money,2))+' dollars by betting on '+option_temp+' in '+options_multi[i]+'.'
        
        
    elif df2.iloc[0,1]==option_temp:
        a1=df[['Away win odds']].loc[df['Fixture:']==options_multi[i]]
        t1=a1.iloc[0,0]
        
        b1=df[['Away Win']].loc[df['Fixture:']==options_multi[i]]*100
        t2=b1.iloc[0,0]
        money=(t1-1)*option_mtemp
        
        option_poss_win=option_poss_win.append({'Moneywon': round(money,2)}, ignore_index=True)
        option_prob_win=option_prob_win.append({'Probwin': round(t2,2)/100}, ignore_index=True)
        
        if option_mtemp != 0:
            'You have a '+str(round(t2,2))+'% chance of winning '+str(round(money,2))+' dollars by betting on '+option_temp+' in '+options_multi[i]+'.'
        
    
    else:
        a1=df[['Draw odds']].loc[df['Fixture:']==options_multi[i]]
        t1=a1.iloc[0,0]
        
        b1=df[['Draw']].loc[df['Fixture:']==options_multi[i]]*100
        t2=b1.iloc[0,0]
        money=(t1-1)*option_mtemp
        
        option_poss_win=option_poss_win.append({'Moneywon': round(money,2)}, ignore_index=True)
        option_prob_win=option_prob_win.append({'Probwin': round(t2,2)/100}, ignore_index=True)
        
        if option_mtemp != 0:
            'You have a '+str(round(t2,2))+'% chance of winning '+str(round(money,2))+' dollars by betting on a draw in '+options_multi[i]+'.'
        


combinations=np.zeros((2**len(options_multi),len(options_multi)))            
for i in range(2**len(options_multi)):
    temp=i
    for j in range(len(options_multi)):
        q=temp//2
        mod=temp%2
        combinations[i,j]=mod
        temp=q
 
prob_dist=pd.DataFrame(columns=['Winning','Probability'])       
for i in range(2**len(options_multi)):
    probability=1
    winning=0
    for j in range(len(options_multi)):
        if combinations[i,j]==1:
            probability=probability*option_prob_win['Probwin'].iloc[j]
            winning=winning+option_poss_win['Moneywon'].iloc[j]
        else:
            probability=probability*(1-option_prob_win['Probwin'].iloc[j])
            winning=winning-option_amount['Moneybet'].iloc[j]
            
    prob_dist=prob_dist.append({'Winning':winning,'Probability':probability}, ignore_index=True)
    
prob_dist=prob_dist.sort_values(by='Winning',ascending=True)
#prob_dist


if prob_dist.shape[0]>1:   
    d=alt.Chart(prob_dist).mark_bar().encode(
        x='Winning',
        y='Probability'
    )
    
    st.altair_chart(d)
    
    expecval=0
    
    for i in range(prob_dist.shape[0]):
        expecval=expecval+prob_dist.iloc[i,0]*prob_dist.iloc[i,1]
    
    'The expected value of your bets is '+str(round(expecval,2))+' dollars.'

    
#option_poss_win
#option_prob_win