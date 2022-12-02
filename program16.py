#!/usr/bin/env python
# coding: utf-8

# In[5]:


def add(num):
    s=0
    for i in range(1,num+1):
        s=s+i
    return s
n=int(input("Enter the limit"))
z=add(n)
print("Sum is:")
print(z)


# In[ ]:




