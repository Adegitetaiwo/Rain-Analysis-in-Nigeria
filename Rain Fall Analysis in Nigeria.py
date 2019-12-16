#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


January = 1
February = 2
March = 3
April = 4
May =5
June = 6
July =7
August = 8 
September = 9 
October = 10
November = 11
December = 12
Months = [January, February, March, April, May, June, July, August, September, October, November, December]


# In[3]:


#Alimosho
Mean_values_Alimosho = [45.53333333, 153, 259.8666667, 346.0666667, 430.2666667, 354.6666667, 152.6666667, 51.6, 149.4666667, 238.1333333, 164.8, 49.46666667]

plt.plot(Months, Mean_values_Alimosho, label = 'LgIsland')
plt.xlabel('Months')
plt.ylabel('Mean Values')
plt.legend()
plt.title('Alimosho')


# In[4]:


#Lg_island
Mean_values_LgIsland = [56.8, 129.2, 217.2, 338.1333333, 439.4, 434.6666667, 176.3333333, 53.13333333, 148.4666667, 216, 112.1333333, 35.33333333]

plt.plot(Months,Mean_values_LgIsland, 'g', label = 'LgIsland')
plt.xlabel('Months')
plt.ylabel('Mean Values')
plt.legend()
plt.title('Lagos island')


# In[5]:


#Epe
Mean_values_Epe = [56.86666667, 136, 251.0666667, 351, 421.6666667, 384.6666667, 191.4666667, 87.53333333, 200.0666667, 230.3333333, 144, 32.66666667]

plt.plot(Months, Mean_values_Epe, 'b', label = 'Epe')
plt.xlabel('Months')
plt.ylabel('Mean Values')
plt.legend()
plt.title('Epe')


# In[6]:


#Ikorodu
Mean_values_Ikorodu = [58.8, 142.9333333, 257.1333333, 350.2666667, 451.8666667, 386.4666667, 161.8, 54.93333333, 169.0666667, 220.4666667, 124.4666667, 42.4]

plt.plot(Months, Mean_values_Ikorodu, 'orange', label = 'Ikorodu')
plt.xlabel('Months')
plt.ylabel('Mean Values')
plt.legend()
plt.title('Ikorodu')


# In[7]:


#Ikeja
Mean_values_Ikeja = [50.46666667, 150.0666667, 245.2666667, 348.0666667, 442.8666667, 379.9333333, 164.5333333, 49.93333333, 151.4666667, 231.9333333, 141, 38.13333333]

plt.plot(Months, Mean_values_Ikeja, 'grey', label = 'Ikeja')
plt.xlabel('Months')
plt.ylabel('Mean Values')
plt.legend()
plt.title('Ikeja')


# In[8]:


#Lg_Mainland
Mean_values_Lg_Mainland = [42.86666667, 145.5333333, 220.2, 320, 415, 426.2666667, 166, 46.13333333, 135.7333333, 214.2666667, 127.9333333, 37.6]

plt.plot(Months, Mean_values_Lg_Mainland, 'mediumseagreen', label = 'Lg_Mainland')
plt.xlabel('Months')
plt.ylabel('Mean Values')
plt.legend()
plt.title('Lagos mainland')


# In[9]:


#Badagry
Mean_values_Badagry = [33.2, 131.2666667, 187.6, 269.3333333, 425.1333333, 376.1333333, 106.6, 33.73333333, 124.2666667, 196.7333333, 90.4, 22.93333333]

plt.plot(Months, Mean_values_Badagry, 'black', label = 'Badagry')
plt.xlabel('Months')
plt.ylabel('Mean Values')
plt.legend()
plt.title('Badagry')


# In[10]:


#Graph of months against mean_values for all Locations

plt.plot(Months, Mean_values_Alimosho, label = 'alimosho')
plt.plot(Months,Mean_values_LgIsland, 'r', label = 'LgIsland')
plt.plot(Months, Mean_values_Epe, 'b', label = 'Epe')
plt.plot(Months, Mean_values_Ikorodu, 'orange', label = 'Ikorodu')
plt.plot(Months, Mean_values_Ikeja, 'grey', label = 'Ikeja')
plt.plot(Months, Mean_values_Lg_Mainland, 'mediumseagreen', label = 'Lg_Mainland')
plt.plot(Months, Mean_values_Badagry, 'black', label = 'Badagry')
plt.plot(Months, Mean_values_Badagry, 'black', label = 'Badagry')
plt.xlabel('Months')
plt.ylabel('Mean Values')
plt.legend()

plt.title('')

