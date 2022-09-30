#!/usr/bin/env python
# coding: utf-8

# In[22]:


# -----------------------------------
# TEST CASE TYPE REFERENCE INFORMATION
# -----------------------------------

uid = 'UID-551' 
theme = 'Names where Name Parts are Modified'
category = 'Character Addition'
sub_category = '1 Character addition at the middle'
entity_type = 'Vessel'

# ********************


# In[2]:


import pandas as pd
from test_case_generator_functions import alphabet

# download the OFAC list from the web

ofac_list_download = pd.read_csv('https://www.treasury.gov/ofac/downloads/sdn.csv', header=None)
ofac_list = ofac_list_download[[0,1,2]]
ofac_list.columns = ['uid', 'name', 'entity_type']


# In[15]:


import random


# In[30]:


ofac_list_filtered = ofac_list[(ofac_list.entity_type == 'vessel')] # only evaluate individuals
ofac_list_filtered = ofac_list_filtered[(ofac_list_filtered.name.str.count(' ') > 1)] # only evaluate names with more than 2 words
ofac_list_filtered = ofac_list_filtered[(ofac_list_filtered.name.str.count(' ') < 4)] # only evaluate names with more than 2 words


# In[31]:


ofac_list_filtered


# In[32]:


ofac_list_sampled = ofac_list_filtered.sample(n = 10)
ofac_list_sampled


# In[33]:


# create blank final test cases table

final_test_cases = pd.DataFrame(columns=['UID', 'Theme','Category','Sub-category','Entity-Type','Test Case ID' , 'OFAC List UID', 'Original Name','Test Case Name'])
final_test_cases


# In[34]:


#seperate for first two words and the last part;
#add random additional character after the second word, and then attach the other part of the name


# In[35]:


# run loop to generate the test cases

for index, row in ofac_list_sampled.iterrows():
        number_of_words = row['name'].count(' ') + 1 # determine for each name the number of words
        if number_of_words == 3:
            name_words=row['name'].split()
            final_test_name=name_words[0]+' '+name_words[1]+random.choice(alphabet())+' '+name_words[2]# create the test case
            final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name] # append to the dataframe
        if number_of_words == 4:
            name_words=row['name'].split()
            final_test_name=name_words[0]+' '+name_words[1]+random.choice(alphabet())+' '+name_words[2]+' '+name_words[3]# create the test case
            final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name] # append to the dataframe
        


# In[36]:


final_test_cases


# In[ ]:




