#!/usr/bin/env python
# coding: utf-8

# In[1]:


try: 
    a = int(input("Enter a:")) 
    b = int(input("Enter b:")) 
    c = a/b 
    print("a/b = %d"%c) 
except Exception: 
    print("Can't divide by zero") 
    print(Exception) 
else: 
    print("Hi I am else block")


# In[ ]:




