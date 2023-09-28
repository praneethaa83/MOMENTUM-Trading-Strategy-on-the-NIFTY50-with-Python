#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[2]:


pip install yfinance


# In[3]:


import yfinance as yf
import numpy as np
import pandas as pd


# In[6]:


stocks = pd.read_html('https://en.wikipedia.org/wiki/NIFTY_50')[2].Symbol


# In[7]:


stocks.head(5)


# In[8]:


stocks = stocks + '.NS'


# In[9]:


stocks = stocks.to_list()


# In[12]:


df = yf.download(stocks,start='2012-01-01')['Close']


# In[13]:


df


# In[14]:


ret_df = df.pct_change()


# In[15]:


ret_df


# In[16]:


mtl_ret = (ret_df +1).resample('M').prod()


# In[17]:


mtl_ret


# In[19]:


mtl_12 = mtl_ret.rolling(12).apply(np.prod).dropna()


# In[20]:


mtl_12


# In[21]:


top_ = mtl_12.loc['2012-12-31'].nlargest(5)


# In[22]:


top_


# In[23]:


top_.name


# In[24]:


mtl_ret[top_.name:][1:2]


# In[25]:


relevant_ret = mtl_ret[top_.name:][1:2][top_.index]


# In[26]:


relevant_ret


# In[27]:


relevant_ret.mean(axis=1)


# In[28]:


def top_performers(date):
    all_ = mtl_12.loc[date]
    top = all_.nlargest(5)
    relevant_ret = mtl_ret [top.name:][1:2][top.index]
    return (relevant_ret).mean(axis=1).values[0]


# In[29]:


top_performers('2012-12-31')


# In[30]:


mom_ret = []
for date in mtl_12.index[:-1]:
    mom_ret.append(top_performers(date))


# In[31]:


pd.Series(mom_ret)


# In[32]:


pd.Series(mom_ret).prod()


# In[33]:


nifty = yf.download('^NSEI',start = '2012-01-01')['Close']


# In[34]:


(nifty.pct_change() + 1).prod()


# In[ ]:




