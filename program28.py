#!/usr/bin/env python
# coding: utf-8

# In[1]:


def getmax(b):
    return max(b,key=len)
a=[]
n= int(input("Enter the number of elements in list:"))
for x in range(0,n):
    e=input("Enter Element : ")
    a.append(e)
print("The Longest word in the list is :", getmax(a))    


# In[ ]:




