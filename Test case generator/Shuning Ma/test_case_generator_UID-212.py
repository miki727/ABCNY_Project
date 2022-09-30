#!/usr/bin/env python
# coding: utf-8

# # IMPORT DATA, PACKAGES, AND FUNCTIONS

# ## import the relevant functions and packages

# In[1]:


import pandas as pd
import numpy as np
from test_case_generator_functions import special_characters, alphabet


# # TEST CASE TYPE REFERENCE INFORMATION

# In[2]:


uid = 'UID-212' 
theme = 'Names where name parts are Modified'
category = 'Character replaced by Number and Special Character'
sub_category = '1 Letter replaced by number and 1 letter replaced by special character'
entity_type = 'Individual'


# ## download the OFAC list from the web

# In[3]:


ofac_list_download = pd.read_csv('https://www.treasury.gov/ofac/downloads/sdn.csv', header=None)


# In[4]:


ofac_list = ofac_list_download[[0,1,2]]
ofac_list.columns = ['uid', 'name', 'entity_type']


# # FILTER FOR THE REQUIREMENTS OF THE TEST CASE TYPE

# ## filter for the requirements of the specific test case type

# In[5]:


ofac_list_filtered = ofac_list[(ofac_list.entity_type == 'individual')] # only evaluate individuals


# ## randomly choose 10 rows

# In[6]:


ofac_list_sampled = ofac_list_filtered.sample(n = 10)


# # CREATE THE TEST CASES

# ## create blank final test cases table

# In[7]:


final_test_cases = pd.DataFrame(columns=['UID', 'Theme','Category','Sub-category','Entity-Type','Test Case ID' , 'OFAC List UID', 'Original Name','Test Case Name'])


# ## run loop to generate the test cases

# In[8]:


for index, row in ofac_list_sampled.iterrows():
    original_name = row['name']

    replace_list = [] # get index of alphabets in each name
    for i in range(len(row['name'])):
        if row['name'][i].upper() in alphabet():
            replace_list.append(i)
    
    replace_id = np.random.choice(replace_list) # replace 1 random alphabet with special character
    temp_name = original_name[:replace_id] + np.random.choice(special_characters()) + original_name[replace_id + 1:]
    replace_list.remove(replace_id)
    
    replace_id = np.random.choice(replace_list) # replace 1 random alphabet with number
    final_test_name = temp_name[:replace_id] + str(np.random.randint(10)) + temp_name[replace_id + 1:]
    
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name] # append to the dataframe

