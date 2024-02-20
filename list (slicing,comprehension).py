#!/usr/bin/env python
# coding: utf-8

# In[3]:


#3 
n1=[2,3,5,6]
n2=[7,8,2]
Multiplication=[]
for i in range(len(n2)):
    for j in range(len(n1)):
        multi=n1[j]*n2[i]
        Multiplication.append(multi)
print(Multiplication)        


# In[4]:


n1=[2,3,5,6]
n2=[7,8,2]
Multiplication=[]
for i in range(len(n2)):
    
        multi1=n1[0]*n2[i]
        Multiplication.append(multi1)
        multi2=n1[1]*n2[i]
        Multiplication.append(multi2)
        multi3=n1[2]*n2[i]
        Multiplication.append(multi3)
print(Multiplication)  


# In[6]:


#list slicing
n=[1,2,3,4.5,"python"]
n[:]     #single slice
n[2:5]   #2 to 4
n[:5]    #0 to 4
n[2:]    #2 to last
print(n[:])
print(n[2:5])
print(n[2:])
print(n[:5])
print(n[-5:-2])
print(n[-5:])
print(n[:-2])
print(n[:])


# In[18]:


# 3 ta parameter 
n=[1,2,3,4,5,6,7,8]
print(n[2:6:1])
print(n[::1])
print(n[:4:1])
print(n[3::1])


# In[21]:


#square

n=[1,2,3,4]
Squarelist=[]
for i in range(len(n)):
    Squarelist.append(n[i]*n[i])
print(Squarelist)    



# In[22]:


#square

n=[1,2,3,4]
Squarelist=[]
for i in range(len(n)):
    Squarelist.append(n[i]**2)
print(Squarelist)    



# In[24]:


#root

from math import sqrt
n=[1,2,3,4]
li=[]
for i in range(len(n)):
    s=sqrt(n[i])
    li.append(s)
print(li)    


# In[ ]:


#Syntex

# Newlist=[expression(Element) for element in oldlist if condition]


# In[26]:


###list comprehension(simplify kora ba sohoj kora)

#list to list
n=[1,2,3,4,5]
squareValue=[n[x]**2 for x in range(len(n))]
print(squareValue)


# In[27]:


###list comprehension(simplify kora ba sohoj kora)

#list to list
#use condition

n=[1,2,3,4,5]
squareValue=[n[x]**2 for x in range(len(n)) if len(n)>0]
print(squareValue)



# In[36]:


###list comprehension(simplify kora ba sohoj kora)

#list to list
#use condition

n=[1,2,3,4,5,3,4,5,6,7,89]
squareValue=[n[x]**2 for x in range(len(n)) if (n[x]%2==0)]
print(squareValue)




# In[ ]:




