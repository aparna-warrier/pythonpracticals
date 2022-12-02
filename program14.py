#!/usr/bin/env python
# coding: utf-8

# In[2]:


a=int(input("Enter a first value"))
b=int(input("Enter a second value"))
print("prime number in range are:")
for number in range(a,b +1):
    if number>1:
        for i in range(2,number):
            if (number%i)==0:
                break
        else:
            print (number)


# In[ ]:




