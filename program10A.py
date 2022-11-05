#!/usr/bin/env python
# coding: utf-8

# In[4]:


num=int(input("enter a number:"))
n=num
sum=0 
a=len(str(num))
while n>0:
    digit=n%10
    sum+=digit**a
    n//=10
if num==sum:
    print(num,"is a armstrong number:")
else:
    print(num,"is not a armstrong number")


# In[ ]:




