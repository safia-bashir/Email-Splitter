#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Email splitter for separating the username and domain name

# Method 1 

# intializing the email 
email =input("Enter Your Email address: ").strip()



# separating the username and the domain name using slicing: 
user= email[0:email.index('@')]
domain=email[email.index('@')+1:]

# printing the result :
print('the username is:' +str(user) )
print('the domain is:'+str (domain) )


# In[ ]:


#Email splitter for separating the username and domain name
# Method 2
# intializing the email 
email =input("Enter Your Email address: ").strip()


# separating the username and the domain name using split method : 
user_name=email.split('@')[0]
domain=email.split('@')[1]

# printing the result :
print('the username is:' +str(user) )
print('the domain is:'+str (domain) )


# In[ ]:




