#!/usr/bin/env python
# coding: utf-8

# In[6]:


year=int(input("enter the year"))
if year%400==0:
    print("leap year")
elif year%4==0 and year%100!=0:
    print("leap year")
else:
    print("not leap year")


# In[ ]:





# In[ ]:




