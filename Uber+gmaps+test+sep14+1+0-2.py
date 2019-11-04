
# coding: utf-8

# In[1]:

import matplotlib.pylab as plt
import gmaps
import pandas as pd
gmaps.configure(api_key="AIzaSyC5qMG6RjQKVQQmnGjtIxmSioxYhrFm52k")


# In[2]:

df = pd.read_csv('../input/uber-raw-data-sep14.csv')


# In[3]:

df.head()


# In[4]:

#len(df)


# In[5]:

df = df[["Date/Time", "Lat", "Lon"]]


# In[6]:

df.head()


# In[7]:

import datetime

start_time = datetime.datetime(year=2014, month=9, day=1, hour=0)
end_time = datetime.datetime(year=2014, month=9, day=1, hour=2)


# In[8]:

df["Date/Time"] = pd.to_datetime(df["Date/Time"])


# In[9]:

#df.head()


# In[10]:

mask = (df["Date/Time"] > start_time)& (df["Date/Time"] < end_time)


# In[11]:

#df.columns


# In[12]:

df.columns = ['time', 'latitude', 'longitude']


# In[13]:

df.head()


# In[14]:

df_0_2 = df.loc[mask]
df_0_2


# In[15]:

locations = df_0_2[['latitude', 'longitude']]
locations


# In[16]:

fig = gmaps.figure()
fig.add_layer(gmaps.heatmap_layer(locations))
fig


# In[ ]:



