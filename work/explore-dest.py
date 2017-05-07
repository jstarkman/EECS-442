
# coding: utf-8

# In[90]:

import re
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
get_ipython().magic('matplotlib inline')


# |Column|Title|
# |------|:-----|
# |1|srch_destination_id
# |2|srch_destination_name
# |3|srch_destination_type_id
# |4|srch_destination_latitude
# |5|srch_destination_longitude
# |6--144|popular_foo|

# In[133]:

dest = pd.read_table("../dest.txt", delimiter="\t", encoding="utf-8", header=0)
data = pd.read_table("../data.txt", delimiter="\t", encoding="utf-8", header=0)


# In[33]:

dest


# In[134]:

data


# ## What do the data look like?

# In[77]:

def plot_map_subregion(ca = 41.5, co = -81.7, cpm = .3):
    """
    Draw a (2*cpm by 2*cpm) scatterplot of a Mercator-ish map centered on (ca, co).
    """
    lonband = dest[dest.srch_destination_longitude.between(co-cpm, co+cpm)]
    region = lonband[lonband.srch_destination_latitude.between(ca-cpm, ca+cpm)]
    plt.scatter(region.srch_destination_longitude, region.srch_destination_latitude)


# In[87]:

plot_map_subregion(cpm=1)


# ## Selecting all rows within a certain distance of a location:

# ### Cheap but ineffective: By city name

# In[14]:

dest.loc[dest.srch_destination_name.str.contains("Cleveland")] # 31 rows


# ### More expensive but more accurate: haversine

# In[24]:

def np_get_distance(lats, lons, center_lat, center_lon):
    """
    Return Numpy array of distances from center.
    https://en.wikipedia.org/wiki/Haversine_formula
    lats, lons are Series; center_foo are floats
    """
    lats_rads, lons_rads = np.radians(lats), np.radians(lons)
    center_lat_rads = math.radians(center_lat)
    center_lon_rads = math.radians(center_lon)
    hs_lon = np.square(np.sin(0.5*(lons_rads - center_lon_rads)))
    hs_lat = np.square(np.sin(0.5*(lats_rads - center_lat_rads)))
    dists = 6367 * 2 * np.arcsin(np.sqrt(         hs_lat + math.cos(center_lat_rads) * np.cos(lats_rads) * hs_lon ))
    return dists


# In[36]:

def np_within_distance(ids, lats, lons, center_lat, center_lon, dist_km):
    """
    Return Series of ids <= dist_km of center.  Calls np_get_distance().
    ids is Series; dist_km is float
    """
    dists = np_get_distance(lats, lons, center_lat, center_lon)
    return pd.Series(ids[dists <= dist_km])


# In[37]:

cle = np_within_distance(dest.srch_destination_id,                    dest.srch_destination_latitude,                    dest.srch_destination_longitude,                   41.5, -81.7, 30)


# In[45]:

cle_full = pd.DataFrame(cle).merge(dest, on="srch_destination_id")


# In[48]:

cle_full


# ## Grouping by country

# ### Simple version: extract country names from `dest.txt`

# In[127]:

RE_COUNTRY = re.compile("^(.*, )?(.*?)( \(.*\))?\s*$")
get_country = lambda name: RE_COUNTRY.search(name).group(2)
countries = dest.srch_destination_name.apply(get_country)
dest["srch_destination_name_country"] = countries


# In[132]:

gb = dest.groupby("srch_destination_name_country")
gb.srch_destination_id.nunique()


# ### SQL version: getting country names from `data.txt` and making them an extra column in dest

# In[135]:

# pd.merge(dest, data)


# ## PCA

# In[80]:

pca = PCA(n_components=2)
pca.fit(10**dest.iloc[:,5:])


# In[81]:

pca.components_[:,:10]


# In[82]:

plt.scatter(pca.components_[0,:], pca.components_[1,:])


# In[6]:

np.argmax(pca.components_[0,:])

