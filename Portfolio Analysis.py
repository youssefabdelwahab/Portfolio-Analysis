#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import pandas_datareader as pdr 
import datetime as dt 
import numpy as np 
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


tickers = ['KO', 'FB']
start = dt.date(2015,8,20)
end = dt.date(2019,11,8)
prices = pdr.data.get_data_yahoo(tickers, start, end)['Adj Close']
prices


# In[3]:


daily_return = prices.pct_change()
daily_return


# In[4]:


mean_return = daily_return.mean()
mean_return


# In[5]:


cov_matrix = daily_return.cov()*250
cov_matrix


# In[44]:


p_weight = []

p_return = []
p_volatility = []
rf= 0.0194
number_assets = len(prices.columns)
number_port= 1000


# In[45]:


for portfolio in range(number_port): 
    weights = np.random.random(number_assets)
    weights = weights/np.sum(weights)
    p_weight.append(weights)
    returns = np.sum(daily_return.mean() * weights)*250
    p_return.append(returns)
    var= cov_matrix.mul(weights, axis=0).mul(weights, axis=1).sum().sum()
    sd=np.sqrt(var)
    annual_sd = sd*np.sqrt(250)
    p_volatility.append(annual_sd)

weights
    


# In[46]:


data = {"Return":p_return, "Volatility":p_volatility}


# In[47]:


for counter , symbol in enumerate(prices.columns.tolist()):
    data[symbol + 'weight']= [w[counter] for w in p_weight]


# In[48]:


portfolio = pd.DataFrame(data)
portfolio 


# In[49]:


portfolio.plot.scatter(x="Volatility", y="Return", grid=True)


# In[50]:


p_sharpe= ((portfolio['Return']-rf)/portfolio['Volatility'])
p_sharpe


# In[29]:


#Tangecy Portfolio
((portfolio['Return']-rf)/portfolio['Volatility']).idxmax()


# In[30]:


portfolio.iloc[((portfolio['Return']-rf)/portfolio['Volatility']).idxmax()]


# In[ ]:


# Portfolio #432 is optimal becuase it satitfies the idmax argument for the highest sharpe ratio given the level of volatility by the amount of weights in each stock 


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




