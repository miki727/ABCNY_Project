#!/usr/bin/env python
# coding: utf-8

# # IMPORT DATA, PACKAGES, AND FUNCTIONS

# ## import the relevant functions and packages

# In[1]:


import pandas as pd
import numpy as np
from test_case_generator_functions import alphabet


# # TEST CASE TYPE REFERENCE INFORMATION

# In[2]:


uid = 'UID-233' 
theme = 'Names where name parts are Modified'
category = 'Repetitions'
sub_category = '1 letters repeated twice'
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
    
    final_test_name = original_name_list.copy()
    
    repeat_list = [] # get index of alphabets in each name
    for i in range(len(original_name)):
        if original_name[i] in alphabet():
            repeat_list.append(i)
    
    random_index = np.random.choice(repeat_list) # randomly choose letter to be repeated
    repeat_list.remove(random_index) # remove chosen letter

    final_test_name[random_index] += original_name_list[random_index] + original_name_list[random_index] # add repeated letter twice

    final_test_name = ''.join(final_test_name)
    
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name] # append to the dataframe

final_test_cases

