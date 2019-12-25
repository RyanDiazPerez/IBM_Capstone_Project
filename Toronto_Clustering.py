#!/usr/bin/env python
# coding: utf-8

# <h1 align=center><font size = 5>Toronto Clustering Assignment by Ryan Diaz-Perez</font></h1>

# <h1 align=left><font size = 4>Part 1: Web Scraping</font></h1>

# In[1]:


get_ipython().system('conda install lxml --yes')
get_ipython().system('conda install html5lib --yes')
get_ipython().system('conda install -c conda-forge beautifulsoup4 --yes')


# In[2]:


import numpy as np # library to handle data in a vectorized manner
import pandas as pd # library for data analsysis
from sklearn.cluster import KMeans # import k-means from clustering stage
import html5lib
from bs4 import BeautifulSoup
import lxml


# <Big><b>Extracting data from the Wikipedia page</b></Big>

# In[3]:


url = "http://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M"
df_toronto = pd.read_html(url, flavor='html5lib')[0]

# Removing rows with Borough value of Not assigned
df_toronto.drop(df_toronto.index[df_toronto['Borough'] == 'Not assigned'], inplace = True)
df_toronto.head()


# In[4]:


# Combining rows
df_toronto = df_toronto.groupby(by=['Postcode','Borough']).agg(lambda x: ','.join(x))
df_toronto.reset_index(level=['Postcode','Borough'], inplace=True)
df_toronto.head(210)


# In[5]:


df_toronto.loc[df_toronto['Neighbourhood'] == ('Not assigned'), 'Neighbourhood'] = df_toronto['Borough']
df_toronto.head(90)


# In[6]:


df_toronto.shape


# <h1 align=left><font size = 4>Part 2: Geographical locations</font></h1>

# In[25]:


# Latitude and Longitude of the neighborhoods
df_geography = pd.read_csv('Geospatial_Coordinates.csv')
df_geography.head()


# In[26]:


# Renaming colunm from Postal Code to Postcode
df_geography.rename({'Postal Code': 'Postcode'}, axis=1, inplace=True)
df_geography.head()


# In[27]:


# Merging df_toronto and df_geography
df_merged = df_toronto.merge(df_geography, how='left', on='Postcode')
df_merged.rename({'Postcode': 'PostalCode'}, axis=1, inplace=True)
df_merged.head()


# <h1 align=left><font size = 4>Part 3: Maps of the neighborhood</font></h1>

# In[ ]:





# In[ ]:





# In[ ]:




