#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cgi


# In[3]:


form = cgi.FieldStorage()
print('Content-type: text/html\n')
print('<tittle>Reply Page</tittle>')
if not 'user' in form:
    print('<h1>Who are you?</h1>')
else:
    print('<h1> Hello <i> %s</i>!</h1>' % cig.escape(form['user'].value))


# In[ ]:




