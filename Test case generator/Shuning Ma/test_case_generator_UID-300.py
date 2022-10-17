#!/usr/bin/env python
# coding: utf-8

# # IMPORT DATA, PACKAGES, AND FUNCTIONS

# ## import the relevant functions and packages

# In[1]:


import pandas as pd
import numpy as np
from test_case_generator_functions import alphabet, rand_letter


# # TEST CASE TYPE REFERENCE INFORMATION

# In[2]:


uid = 'UID-300' 
theme = 'Names where name parts are Modified'
category = 'Typos'
sub_category = '1 Typo - any letter'
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
ofac_list_sampled


# # CREATE THE TEST CASES

# ## create blank final test cases table

# In[7]:


final_test_cases = pd.DataFrame(columns=['UID', 'Theme','Category','Sub-category','Entity-Type','Test Case ID' , 'OFAC List UID', 'Original Name','Test Case Name'])
final_test_cases


# ## run loop to generate the test cases

# In[8]:


for index, row in ofac_list_sampled.iterrows():
    original_name = row['name'].upper()
    original_name_list = list(original_name) # transfer name string into letter list
    
    random_index = np.random.choice(list(range(len(original_name_list)))[1:-1]) # randomly choose letter to be replaced
    while original_name_list[random_index] not in alphabet(): # rerandom if not letter 
        random_index = np.random.choice(len(original_name_list))
    while original_name_list[random_index] == original_name[random_index]: # rerandom if no letter has been replaced
        original_name_list[random_index] = rand_letter() # replace letter

    final_test_name = ''.join(original_name_list)
    
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name] # append to the dataframe

final_test_cases

