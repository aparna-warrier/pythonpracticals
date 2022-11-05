#!/usr/bin/env python
# coding: utf-8

# In[2]:


a=int(input("enter the first value:"))
b=int(input("enter the second value:"))
op=input("enter operator +,-,*,/,%,^")
if(op=="+"):
    print("Sum is",a+b)
elif(op=="-"):
    print("Difference is",a-b)
elif(op=="*"):
    print("Product is",a*b)
elif(op=="/"):
    print("Quotient is",a/b)
elif(op=="%"):
    print("Remainder is",a%b)
elif(op=="^"):
    print("power is",a**b)
else:
    print("Not recognized operator")


# In[ ]:




