#!/usr/bin/env python
# coding: utf-8

# # IMPORT DATA, PACKAGES, AND FUNCTIONS

# ## import the relevant functions and packages

# In[1]:


import pandas as pd
import numpy as np
from test_case_generator_functions import alphabet, num_of_alphabet, rand_letter


# # TEST CASE TYPE REFERENCE INFORMATION

# In[2]:


uid = 'UID-305' 
theme = 'Names where name parts are Modified'
category = 'Typos'
sub_category = '2 typos different name parts'
entity_type = 'Entity'


# ## download the OFAC list from the web

# In[3]:


ofac_list_download = pd.read_csv('https://www.treasury.gov/ofac/downloads/sdn.csv', header=None)
ofac_list_download


# In[4]:


ofac_list = ofac_list_download[[0,1,2]]
ofac_list.columns = ['uid', 'name', 'entity_type']
ofac_list


# # FILTER FOR THE REQUIREMENTS OF THE TEST CASE TYPE

# ## filter for the requirements of the specific test case type

# In[5]:


ofac_list_filtered = ofac_list[(ofac_list.entity_type == '-0- ')] # only evaluate entities
ofac_list_filtered


# ## randomly choose 10 rows

# In[6]:


while True:
    ofac_list_sampled = ofac_list_filtered.sample(n = 10)
    cnt = [0] * 10
    for ind, name in enumerate(ofac_list_sampled['name']):
        split_name = name.upper().split(' ')
        
        for i in split_name:
            if all(j not in alphabet() for j in i):
                split_name.remove(i) # remove word with all numbers
                
        cnt[ind] += len(split_name)

    if all(i >= 2 for i in cnt):
        break

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
    split_original_name = original_name.split(' ') # split name into word
    
    final_test_name = split_original_name.copy()
    
    split_edit_name = []
    for i in split_original_name:
        if not all(j not in alphabet() for j in i):
            split_edit_name.append(i) # remove word with all numbers
    
    for i in range(2):
        modify_original_name = np.random.choice(split_edit_name) # randomly choose word to be replaced
        modify_index = original_name.split(' ').index(modify_original_name) # record index of chosen word
        split_edit_name.remove(modify_original_name) # remove chosen word
        
        modify_original_name = list(modify_original_name) # split word into letter
        replace_name = modify_original_name.copy()
        
        j = np.random.choice(list(range(len(replace_name))))
        while modify_original_name[j] not in alphabet(): # rerandom if not letter 
            j = np.random.choice(list(range(len(replace_name))))
        while replace_name[j] == modify_original_name[j]: # rerandom if no letter has been replaced
            replace_name[j] = rand_letter() # replace letter
        
        final_test_name[modify_index] = ''.join(replace_name)
    
    final_test_name = ' '.join(final_test_name)
    
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name] # append to the dataframe

final_test_cases

