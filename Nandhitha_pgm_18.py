#!/usr/bin/env python
# coding: utf-8

# In[15]:


def palindrome(n):
    temp=n
    rev=0
    while(n>0):
        d=n%10
        rev=rev*10+d
        n=n//10
    if(temp==rev):
        print("The number is palindrome")
    else:
        print("The number is not palindrome")
n=int(input("Enter the number:"))
palindrome(n)


# In[ ]:




